from foods import targets_min, targets_max, food
import argparse
import json

parser = argparse.ArgumentParser(description='Nutritionally Balanced Ingredient Ratios based on general recipe suggestions')
parser.add_argument('-r', help='Recipe File')
parser.add_argument('-d', nargs='?',const=True, default=False,help='Debug - Tells you what the program is thinking')
parser.add_argument('-o', nargs='?',const=True, default=False,help='Override Nutrient goals with the one in recipe file')
parser.add_argument('-s', nargs='?',const=True, default=False,help='Suggest target nutrients (like override), but allow program to still eliminate nutrients in your suggestion that aren\'t practical')
parser.add_argument('-b', help='Ammount of nutrients to back off on',default=0)
args = parser.parse_args()

# Get the recipe data
if not args.r:
	print("Please specify a recipe file with the -r argument")
	quit()
else:
	ingredients = json.load(open(args.r))

# What you expect to eat in calories daily
metabolized = 1800	

# Initialized data structure of nutrient info of eventual resulting recipe
mealdata = {"calories":0,"carbs":0,"fiber":0,"fat":0,"monofat":0,"polyfat":0,"omega3":0,"omega6":0,"saturatedfat":0,"protein":0,"B1":0,"B2":0,"B3":0,"B5":0,"B6":0,"B12":0,"Biotin":0,"Choline":0,"Folate":0,"Vitamin A":0,"Vitamin C":0,"Vitamin D":0,"Vitamin E":0,"Vitamin K":0,"Calcium":0,"Chromium":0,"Copper":0,"Fluoride":0,"Iodine":0,"Iron":0,"Magnesium":0,"Manganese":0,"Molybdenum":0,"Phosphorus":0,"Potassium":0,"Selenium":0,"Sodium":0,"Zinc":0}


#=====================================================#
# Pre-process most acheivable nutrients to attempt    #
# These next 3 routines work together to acheive this #
#=====================================================#

# Take inventory of maxiumum allowed for each food, to see what nutrients are 'possible' to hit 100% daily value on
# The output will be a dict structure with percent rdi possible for each nutrient (unsorted)
# Caveat, this doesn't consider if you need to eat beyond your daily calorie limit to get a nutrient, just if the nutrient is obtainable in the total food
def goals(ingredients,food,tmin):
	# Get copy of datastructure that has nutrients
	nutrients = targets_min.copy()

	# Remove some macros or other non-goal stuff
	nutrients.pop('calories', None)
	nutrients.pop('carbs', None)
	nutrients.pop('fat', None)
	nutrients.pop('saturatedfat', None)
	nutrients.pop('monofat', None)
	nutrients.pop('polyfat', None)

	# Initiliaze dict of remaining nutrients with zero value
	nutrients = nutrients.keys()
	optimals = dict.fromkeys(nutrients,0)

	# Initilize dict of each food weight (to zero), total hypothetical meal nutrient totals, and init current weight to zero
	mealdata = {"calories":0,"carbs":0,"fiber":0,"fat":0,"monofat":0,"polyfat":0,"omega3":0,"omega6":0,"saturatedfat":0,"protein":0,"B1":0,"B2":0,"B3":0,"B5":0,"B6":0,"B12":0,"Biotin":0,"Choline":0,"Folate":0,"Vitamin A":0,"Vitamin C":0,"Vitamin D":0,"Vitamin E":0,"Vitamin K":0,"Calcium":0,"Chromium":0,"Copper":0,"Fluoride":0,"Iodine":0,"Iron":0,"Magnesium":0,"Manganese":0,"Molybdenum":0,"Phosphorus":0,"Potassium":0,"Selenium":0,"Sodium":0,"Zinc":0}
	nutrient_list = list(mealdata.keys())

	# make a 'recipe' with all of the foods thrown in	
	for ingredient_val in ingredients['ingredients']:					# For each ingredient
		weight = ingredients['ingredients'][ingredient_val]['max']			# get weight of max allowed for food as defined by recipe
		multiplier = (1/500) * weight										# adjust weight due to food definitions being in 500g
		# Add the ammount
		for nutrient in nutrient_list:										# For each nutrient
			nutrivalue = food[ingredient_val][nutrient]							# get the nutrient ammount for this food (500g level)
			mealdata[nutrient] += nutrivalue*multiplier							# Affectivley adjust value by dividing by 500 and multiplying by full weight allowed in recipe, then add it to 'meal'

	# Get percentages (RDI) for each nutrient in total of ingredients
	for nutrient in optimals:											# For each nutrient
		rdi = (mealdata[nutrient] / tmin[nutrient]) * 100				# Calculate what the pool of food contributes as the RDI%
		optimals[nutrient] = rdi										# Replace nutrient ammount with RDI%

	return(optimals)		# Returns RDI%'s without sorting or preference

# Assuming you ate nothing but each food to get your daily intake of calories, which nutrients are
# possible to hit.
def optimals(ingredients):
	# Get copy of datastructure that has nutrients
	nutrients = targets_min.copy()

	# Remove some macros or other non-goal stuff
	nutrients.pop('calories', None)
	nutrients.pop('carbs', None)
	nutrients.pop('fat', None)
	nutrients.pop('saturatedfat', None)
	nutrients.pop('monofat', None)
	nutrients.pop('polyfat', None)

	# Assume every nutrient is suboptimal until proven otherwise
	optimals = dict.fromkeys(nutrients,'no')

	# Get nutrient names
	nutrients = nutrients.keys()

	# For Each nutrient, note if it has a food above or below threshold to get enough of it
	for nutrient in nutrients:
		for ingredient in food:							# For each possible food
			if ingredient in ingredients:				# 	If it's a food in our recipe
				# Get some data
				nutrivalue = food[ingredient][nutrient]	# 		Get nutrient value (at 500g)
				minvalue = targets_min[nutrient]		# 		Get minimum needed for RDI
				calories = food[ingredient]['calories'] # 		Calories (at 500g)

				# Adjust the data for maximum possible of ingredient suggested in recipe
				ratio = ingredients[ingredient]['max']/500	# maximum allowed by recipe divided by 500g
				nutrivalue *= ratio							# nutrient value * above ratio
				calories *= ratio							# calorie ammount * above ratio
				cal_multiplier = metabolized / (calories + 0.01) # calorie ratio to consider daily cal limit, +0.01 to avoid divide by 0

				percent = ((nutrivalue/minvalue)*100) * cal_multiplier	# How much is the RDI considering daily calorie limit
				if percent > 100:						# If it up to or exceeds 100%
					optimals[nutrient] = 'yes'			# Mark this particular nutrient as possible, irregardless of which food done it

	optimal_micros = []							# Init our optimal nutrients
	for optimal in optimals:					# For Each nutrient
		if optimals[optimal] == 'yes':			#	If it's optimal
			optimal_micros.append(optimal)		#		Add it to our list

	# Return the nutrient list of optimal nutrients
	return(optimal_micros)

# Have a ranked list of nutrients that are possible based on maximum ingredients available without 
# going over calorie limit on a particular food that offers the nutrient. This is the sub that
# glues the information together found in the goals() and optimals() subs
def best_nutrients(optimal,goal):
	# Init the nutrients
	optimals = dict()

	for nutrient in optimal:						# For each possible nutrient that can hit an RDI with just one food
		if goal[nutrient] >= 100:					#	If we can get 100% of the nutrient will ALL the food in the pot
			optimals[nutrient] = goal[nutrient]		#		Consider it a target nutrient (not perfect, no garuntees)

	# Sort the nutrients from worst to best, and make a list structure
	optimalssorted = {k: v for k, v in sorted(optimals.items(), key=lambda item: item[1])}	# A ranked list of the hardest to easiest
	optimals = list(optimalssorted.keys())													# Just the list of optimal ingredients to return
	
	# If we notice that the nutrients targeted are falling short from our recipe results. We can dynamically tell this
	# program to leave out the worst performing nutrients, provided with the -b argument in the cli.
	# For example, '-b 3' would ignore the 3 worst performing nutrients from this list
	optimals = optimals[int(args.b):]		# Adjust the ability to back off on harder to hit nutrients

	return(optimals)		# Return the names of nutrients we are ultimately going to target throughout the run of this

# For each nutrient in current ingredients, get a metric for demanded (and shunned) nutrients
# The value will take rdi and weight it be how much it deviates from 100% (done in a non-linear [squred] method)
# More deviated under, higher demand, more deviated above, higher shun
# This sub is where the number crunching magic happens
def nutrient_metrics(mealdata,metabolized,tmin,tmax):

	# Get multiplier
	multiplier = metabolized/(mealdata['calories'] + 0.000000000001) # Since RDI is based on daily caloric intake, have multiplier to account for that, and avoid div by 0

	for nutrient in mealdata:		# For each nutrient
		# Update each nutrient as if it was our full daily meals worth based on current food ratios
		mealdata[nutrient] = mealdata[nutrient] * multiplier		# How much of nutrient to we currently have in our pool of already added ingredients?

		# Calculate Metrics
		if tmin[nutrient] == 0:										# If we don't have minimum preference on nutrient
			mealdata[nutrient] = 0										# We need it 0 amount
		elif mealdata[nutrient] <= tmin[nutrient]:					# If less than RDI
			metric = mealdata[nutrient] / tmin[nutrient]				# Calculate rdi %
			mealdata[nutrient] = ((1-metric)*10)*((1-metric)*10)		# ... (squared, something something)
		elif tmax[nutrient] == 0:									# Otherwise, we're above rdi%, but
			mealdata[nutrient] = 0										# No maximum preference, so score of 0
		elif mealdata[nutrient] > tmin[nutrient]:					# But if we do have max preference (toxicity matters)
			over_range = tmax[nutrient] - tmin[nutrient]				# Give proportional negative score
			over_ammount = mealdata[nutrient] - tmin[nutrient]
			metric = (over_ammount/over_range)*10
			mealdata[nutrient] = 0 - metric*metric

	return(mealdata)	# Return negative/positive values for each nutrient, corresponding to the demand/repulsion for each

# For each relevant nutrient in each food serving value, multiply nutrient rdi with metrics multiplier
# This is step 2 of the magic, use above sub to deduce which of the remaining food servings best fits this criteria
def best_ingredient(metrics,ach_nutr,ingredients,food,tmin):
	best_score = ''		# Init Best Score
	best_food = ''		# Init Best Food
	for ingredient in ingredients:		# For each food ingredient considered
		food_metric = 0
		for nutrient in ach_nutr:		# 	For each acheivable nutrient
			# What RDI amount does this food have?
			value = food[ingredient][nutrient]			# How much of a nutrient
			weight = ingredients[ingredient]['res']		# Serving Size
			multiplier = (1/500) * weight				# Weight Adjustment
			adjusted_value = value * multiplier
			with_metric = adjusted_value * metrics[nutrient]	# Adjusted for need (or avoidance)
			food_metric += with_metric							# Accumulate nutrient score for food

		# See if this is the best food so far
		if best_score == '':
			best_score = food_metric
			best_food = ingredient
		if food_metric > best_score:
			best_food = ingredient
			best_score = food_metric

	return(best_food)					# Return the best food found based on metrics

# A non-critical sub, but if you want to audit this program serving-by-serving, this sub helps
# In displaying why a food was selected. At this point, we are already telling the sub what the
# food was, and how much of each key nutrient (needed and avoid) there is. This sub just displays
# That given data in a friendly way.
def why_the_food(needed,avoid,ingredient,foods,tmin,tmax,recipedata):
	print('We seem to need these the most: ',*needed)
	print('But we need to avoid these: ',*avoid)	
	print('We think a {} gram serving of {} most fits the bill with:\n========================================'.format(recipedata[ingredient]['res'],ingredient))
	for nutrient in needed:
		output = foods[ingredient][nutrient]/500		# Get the nutrient ammount per gram
		output *= recipedata[ingredient]['res']			# multiply by serving ammount
		output /= tmin[nutrient]						# RDI value for serving of food
		print('\t{}: {} - ({:.4f}%)'.format(nutrient,foods[ingredient][nutrient],output))
	print('----------------------------------------')
	for nutrient in avoid:
		output = foods[ingredient][nutrient]/500		# Get the nutrient ammount per gram
		output *= recipedata[ingredient]['res']			# multiply by serving ammount
		output /= tmax[nutrient] + 0.000000000000001	# % to max RDI	(+ very small amount to not div by 0)
		print('\t{}: {} - ({:.4f}% to max)'.format(nutrient,foods[ingredient][nutrient],output))

#=====================================================#
#                 Init Some Data                      #
#=====================================================#
nutrient_list = list(mealdata.keys())
food_weights = dict.fromkeys(ingredients['ingredients'],0)
current_weight = 0

#=====================================================#
# Add the initial minimum required food for each      #
# ingredient                                          #
#=====================================================#
for ingredient_val in ingredients['ingredients']:				# For each ingredient	
	weight = ingredients['ingredients'][ingredient_val]['min']	#	Get the weight (minimum)
	multiplier = (1/500) * weight								#	Adjust for the food definition file 500g quantity
	# Add the ammount
	for nutrient in nutrient_list:								#	For each nutrient in the food
		nutrivalue = food[ingredient_val][nutrient]				#		Get the value
		mealdata[nutrient] += nutrivalue*multiplier				#		Add it into our whole meal
	current_weight += weight									#	Adjust new total weight of meal
	food_weights[ingredient_val] += weight						#	Also each individual food weight

	# And if we want to audit, see how much of each food is being added
	if args.d and weight != 0:
		print('Adding Minimums: Adding {} grams of {}'.format(weight,ingredient_val))

#=====================================================#
# Different ways to override optimal target nutrients #
#=====================================================#
if args.o and args.s:
	print("Please only decide on Override OR Suggest, not both")
	quit()
if args.o:
	acheiveable_nutrients = ingredients['nutrients']	# Literally take the override nutrients
# Use the override ingredients, but still process which ones are still not optimal to use. This is an indirect
# Method to ignore nutrients that you don't care about (due to supplimentation or other meals of the day being stronger in them)
elif args.s:
	acheiveable_nutrients = []
	acheiveable_nutrients_total = best_nutrients(optimals(ingredients['ingredients']),goals(ingredients.copy(),food.copy(),targets_min))
	for nutrient in acheiveable_nutrients_total:
		if nutrient in ingredients['nutrients']:
			acheiveable_nutrients.append(nutrient)
# Otherwise, just let this program work it's own magic
else:
	acheiveable_nutrients = best_nutrients(optimals(ingredients['ingredients']),goals(ingredients.copy(),food.copy(),targets_min))

#=====================================================#
#                  Food Adding Loop                   #
#=====================================================#
# These are the values to stop adding ingredients at (weight, calories, and servings)
fullweight = ingredients['fullweight']
fullcalories = ingredients['fullcalories']
fullservings = ingredients['fullservings']
servings = 0	# So far, we have added no servings, but keep track

# While we haven't gone over any of the recipe limits (weight, calories, or servings), whichever comes first
while current_weight <= fullweight and mealdata['calories'] <= fullcalories and servings <= fullservings :
	# Calculate Needed and Avoidable nutrients
	metric_results = nutrient_metrics(mealdata.copy(),metabolized,targets_min,targets_max)

	# Use that to find what the next best food is
	fooditem = best_ingredient(metric_results,acheiveable_nutrients,ingredients['ingredients'],food,targets_min)

	# Have you reached the maximum for this food?
	if food_weights[fooditem] >= ingredients['ingredients'][fooditem]["max"]:
		# If so, remove the food
		ingredients['ingredients'].pop(fooditem, None)
		food.pop(fooditem, None)
		continue	#next food to try (skip everything below and move on to next serving without this food anymore)

	# Optional Auditing (Explains why each food is selected):
	# -----------------------------------------------------------------
	# If debugging/auditing, display what is needed, needs avoiding, and what food best suits this
	if args.d:
		# Sort the nutrient metrics from most avoidable to most needed
		nutrientrank = {k: v for k, v in sorted(metric_results.items(), key=lambda item: item[1])}
		nutrientrank = list(nutrientrank.keys())	# Make it a list

		# Have a seperate list that only considers the nutrients we are trying to hit
		nutrientrank_acheivable = []
		for nutrient in nutrientrank:
			if nutrient in acheiveable_nutrients:
				nutrientrank_acheivable.append(nutrient)

		# Note that lists are from worst to best
		most_needed = nutrientrank_acheivable[-5:]	# top 5 most needed
		most_avoided = nutrientrank[:5]				# top 5 most repulsive

		# Run the sub that displays these findings nicely
		why_the_food(most_needed,most_avoided,fooditem,food,targets_min,targets_max,ingredients['ingredients'])

	weight = ingredients['ingredients'][fooditem]["res"]	# Get weight of serving
	multiplier = (1/500) * weight							# Adjust for the 500g amount in def file
	for nutrient in nutrient_list:							# For each nutrient
		nutrivalue = food[fooditem][nutrient]				#	Get the amount of the nutrient
		mealdata[nutrient] += nutrivalue*multiplier			# 	Add the proportional serving ammount to the meal pool
	current_weight += weight								# Adjust new weight
	food_weights[fooditem] += weight						# Adjust/Add to weight of ingredient in pool

	# If we're auditing, then display how much of which food we are adding for this serving.
	if args.d and weight != 0:
		print('Additional Serving {}: Adding {} grams of {}\n'.format(servings,weight,fooditem))

	servings += 1		# Check off this serving as done

#=====================================================#
#                  Presentation                       #
#=====================================================#
print("Nutrition Facts:")
calorie_multiplier = metabolized/mealdata['calories']
for nutrient in mealdata:
	print('\t',end='')								# Print an initial tab
	if nutrient in acheiveable_nutrients:			# If the nutrient was one we were trying for
		print('*',end='')							# 	indicate it with a leading '*'
	if targets_min[nutrient] == 0:					# If there isn't a gaol for the nutrient
		print("{:16}{:.9f}".format(nutrient,mealdata[nutrient]))	# Don't bother showing the RDI
	else:
		print("{:16}{:.9f} ({:.2f}%) / ({:.2f}%)".format(nutrient,mealdata[nutrient],(mealdata[nutrient]/targets_min[nutrient])*100,(mealdata[nutrient]/targets_min[nutrient])*100*calorie_multiplier))

print("Ingredients to Add:")
for food in food_weights:
	if food_weights[food] != 0:
		print("\t{}: {} grams".format(food,food_weights[food]))
#print(food_weights)		# How much (in grams) each ingredient to use
print("\tTotal: {}".format(current_weight))	# How heavy the whole recipe ended up being (in grams)

