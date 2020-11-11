Takes your ingredient suggestions and crafts a recipe (portions) that attempts to maximize on nutrition

Usage
====
nutrition_balancer.py [-h] [-r R] [-d [D]] [-o [O]] [-s [S]] [-b B]<br><br>

Nutritionally Balanced Ingredient Ratios based on general recipe suggestions<br><br>

optional arguments:<br>
  -h, --help  show this help message and exit<br>
  -r R        Recipe File<br>
  -d [D]      Debug - Tells you what the program is thinking<br>
  -o [O]      Override Nutrient goals with the one in recipe file<br>
  -s [S]      Suggest target nutrients (like override), but allow program to<br>
              still eliminate nutrients in your suggestion that aren't<br>
              practical<br>
  -b B        Ammount of nutrients to back off on

Configuration Files
====
First, we need a file that has a list of all available foods that we normally expect to by at our own grocery, not exotic shit that we don't. This file also lists the minimum RDI value of each nutrient, and if applicable, the level at which that nutrient becomes toxic. The foods themselves are likely accurate enough, but these RDI values can actually be very individual, based on gender, age, and other things. The sample file in this git is foods.py

Next, we need our actual recipe file, it can be named anything, but it does need to be in json format. First is every ingredient, with a key for minimum, maximum, and serving size (called resolution). Everything is measured in grams. I know its not flexible, and probably not super accurate for fluid measurements, just deal with it. You can use these values to stress that a food is optional (min = 0) or has a required amount (min=required ammount). You can use the 'max' value to set a cap on each ingredient (kale and spinach are healthy, but...). Finally, 'res' is for the serving size; how many beans or olives come in one can or something like that. But if your pouring frozen corn out of a bag, fuckit, set 'res' to 1 (1 gram), It's cool to see super granular proportions.

Below the foods, we also set a cap for weight, calories, and servings, this is how the program knows when to stop adding food. Weight is a cludgy substitute for volume, I focus on this limit for something like a chili recipe (put in enough food to fill to pot, calories and servings be damned). I like using servings for a situation where I'm ordering something like a salad online, and can pick up to (lets say) 8 ingredients. You can also have the program stop at a specific calorie limit as well.

How It Works
====
Tediously, in no way will I say any of this is convenient. This script was just for me, but why not make it public anyway.

The TL;DR is that it incrementally keeps adding servings of your foods defined in a recipe file based on which food best satisfies the demanded nutrient profile.

That's an oversimplification obviously.

First, before it does anything worth thinking about, it considers all of the foods in your recipe that have minimum required ammounts and adds them without thought, because that is what you demanded by putting those minimums in your recipe file.

Also before getting into a loop on adding additional servings, it will preprocess what nutrients it thinks are going to be the most practical to target; to play to the strengths of the ingredients in the recipe. In other words, what fucking sense does it make to look at a list of vegetables, see that our meal is currently lacking in vitamin B12, and keep trying to add foods that have the most of that. The rest of the vitamins and minerals that vegegtables play well to might get neglected (or more likely, off balance).

The nutrient preprocessing is attacked from a couple of angles. One way to look at it is to just fill up the whole bag with the maximum ammounts (as defined in our recipe file) of each food, and to see if we can even acheive 100% or more rdi of any of the nutrients. Another way is to look at each food, and see if we hypothetically ate our daily calorie limit in just that food, which nutrients can we get to 100% or more on. The preprocessing considers both of these methods.

Of course, you can override this in the recipe file by listing the nutrients you care about. You can either do a full override (-o flag), which takes these nutrients at face value, or you can do a suggested (-s flag) override. The -s override is more of an indirect ignoring of nutrients. What this does is takes your list, and uses that for the same preprocessing routines (so it will still eliminate the ones that it doesn't think it can hit). But you can use -s to explicitely not include stuff like B vitamins if you heavily consume nutritional yeast, or omega 3 if you take a suppliment for it, or a whole profile of nutrients if you plan on eating a different meal that day that already satsifies for them. The -o/-s customizations are pretty much a required flexibility for any of this to have any practical use.

As an additional cool tweek, say you run into a situation where it still seems like it's failing to hit about 3 of the target nutrients. If this is the case, use the -b argument as '-b 3', and it will ignore the 3 least performing nutrients. You can pick other numbers than 3, picking 0 would effectively be the same as not using the argument at all. Note that 'targetted' nutrients have an '*' preceding them in the program output, to more easily identify them.

Now that we know which nutrients we want to target (and have already added our minimum food to the pot), we need to know which nutrients we are currently lacking the most, and possibly which ones we are getting too close to for toxicity. There is a subroutine that notes all of this but doesn't weight it in a linear way (it uses a squared method). In other words, consider if we have 35% of Zinc and 70% of Pottassium already. This program isn't going to say that it needs Zinc twice as much (as it has half as much as Zinc), long story short, it will be exponentially hungrier for Zinc than Pottassium. This logic works the same way as a nutrient is approaching toxicity (it will get exponentially larger negative values as it approaches).

At the point that we have coded numerical values for our nutrition needs, we then go through each food, note the nutrient ammounts and multiply out by each of these metrics and add to a total for each food. Whichever food has the highest score (for that proportional servings size of course), wins, and that is the next ingredient of that serving we add.

The Full Package
====
It's interesting to think about what the best proportions of grains to use for a cerial. As in how much percent of oats to amaranth to barely, etc... But if you are going to take that efficient blend and then add toppings to it, like berries and nuts, then asking what the best grain blend is, is the wrong question. The moment you add a little bit of walnuts to the top, it changes the nutrition profile. Specifically, just considering the grain blend, maybe you were spinning your wheels trying to get copper, you picked the right grains to maximize, then you add walnuts and push yourself over the edge. If you factor in the walnuts AND the grains, you can pick proportions even more wisely. If you have a recipe file with all the grains, all the nuts, all the berries, and whatever other mix-ins, you can get more than just 'a part of a balanced breakfast,' it IS the balanced breakfast.

Use-Case
====
There are a couple .recipe files included for reference, I can talk through the salad.recipe file. In this use-case, I am ordering a salad from my bodega. There are a few different options for which type of salad (iceberg, spinach, mixed, etc...). I included all the amounts of 'salad' leaves as non-optional (min value defined) servings. I added olive oil as the dressing.

There are many other ingredients to choose from, I didn't list them all in my recipe file, just the ones that I am okay with eating (I left all of the meat and dairy options out). I gave the smallest cap on servings, I set it to 6 (starts counting from 0 though). The serving count starts AFTER the non-optional ingredients are added. So it effectively means extra servings cap.

When running the program the first time, I noticed that it didn't include broccoli. I added this as a required ingredient and brought my serving count down from 7 to the now 6. I have a personal goal to try and get at least one cruciferous veggie into my face each day, so I overrode the preferences of this program for that. Interestingly, it sacrificed a serving of red bell pepper to squeeze the broccoli in instead. It only made a noticable (10% rdi) difference on vitamin C and vitamin K. Adding broccoli essentially took a small hit on vitamin C but boosted vitamin K instead. This makes sense, vitamin C had not made it to it's rdi goal yet, and vitamin K did, so the program naturally saw red bell pepper as more suitable than broccoli to reach that goal. However, no biggie, broccoli is healthy as fuck, and vitamin C is easy enough to get in another meal.

I also have a very specific list of nutrients listed in the recipe file that I use the -o flag to override with. I explicitely didn't want my program to try for the omegas, as I suppliment. I use nutritional yeast, so don't need the B vitamins (but included B5 as my nooch doesn't have that one). I get my choline from a choline/inositol suppliment. I also suppliment Vitamin D as I'm too high on the hemisphere to always be getting that from the sun. I get plenty of Vitamin E and Calcium in the amount of unsweetened almond chocolate milk I drink in a day. Just one brazil nut is more than enough as a selenium suppliment (and I eat that one brazil nut a day). And sodium? I don't think that's a problem for us to get the MINIMUM of anyway.

It is slightly different than the salad I always ordered before this one, and is nutritionally better consistently down the line compared to it. Though, it's marginally better; like 10%-50% increases for each nutrient, but usually around the 10% range for most. I guess this didn't surprise me, so long as all the ingredients I'm throwing into the bowl are healthy veggies and healthy whole foods, it's kind of hard to fuck up. But why not squeeze that extra 10% of efficiency out of the calories consumed?

Use-Case Output
====
xlogicx$ python3 nutrition_balancer.py -r salad.recipe -o -d<br>
Adding Minimums: Adding 36 grams of lettucegreen<br>
Adding Minimums: Adding 36 grams of lettucered<br>
Adding Minimums: Adding 30 grams of spinach<br>
Adding Minimums: Adding 27 grams of oliveoil<br>
Adding Minimums: Adding 22 grams of broccoli<br>
We seem to need these the most:  Phosphorus fiber protein B5 Zinc<br>
But we need to avoid these:  Vitamin K Folate Iron Manganese omega6<br>
We think a 44 gram serving of kidneybean most fits the bill with:<br>

----------------------------------------
	Phosphorus: 0.605 - (0.0761%)
	fiber: 27.5 - (0.0637%)
	protein: 39.9 - (0.0702%)
	B5: 0.00104 - (0.0183%)
	Zinc: 0.00375 - (0.0300%)

----------------------------------------
	Vitamin K: 3.95e-05 - (0.0017% to max)
	Folate: 0.00014 - (0.0123% to max)
	Iron: 0.0075 - (0.0147% to max)
	Manganese: 0.00192 - (0.0154% to max)
	omega6: 0.6 - (0.0018% to max)
Additional Serving 0: Adding 44 grams of kidneybean<br><br>

We seem to need these the most:  protein Potassium Magnesium B5 Zinc<br>
But we need to avoid these:  Vitamin K Folate Iron Manganese Vitamin C<br>
We think a 41 gram serving of chickpeas most fits the bill with:<br>

----------------------------------------
	protein: 35.25 - (0.0578%)
	Potassium: 0.63 - (0.0152%)
	Magnesium: 0.13 - (0.0254%)
	B5: 0.0012 - (0.0197%)
	Zinc: 0.000315 - (0.0023%)

---------------------------------------
	Vitamin K: 1.7e-05 - (0.0007% to max)
	Folate: 0.00024 - (0.0197% to max)
	Iron: 0.00535 - (0.0097% to max)
	Manganese: 0.00423 - (0.0315% to max)
	Vitamin C: 0.0005 - (0.0000% to max)
Additional Serving 1: Adding 41 grams of chickpeas<br><br>

We seem to need these the most:  protein Magnesium Potassium B5 Zinc<br>
But we need to avoid these:  Vitamin K Manganese Folate Iron Copper<br>
We think a 57 gram serving of avacado most fits the bill with:<br>

----------------------------------------
	protein: 9.8 - (0.0223%)
	Magnesium: 0.145 - (0.0394%)
	Potassium: 2.535 - (0.0850%)
	B5: 0.00732 - (0.1669%)
	Zinc: 0.0034 - (0.0352%)

----------------------------------------
	Vitamin K: 0.000105 - (0.0060% to max)
	Manganese: 0.00075 - (0.0078% to max)
	Folate: 0.000445 - (0.0507% to max)
	Iron: 0.00305 - (0.0077% to max)
	Copper: 0.00085 - (0.0097% to max)
Additional Serving 2: Adding 57 grams of avacado<br><br>

We seem to need these the most:  Phosphorus Potassium protein Magnesium Zinc<br>
But we need to avoid these:  Vitamin K Folate Manganese Iron Copper<br>
We think a 44 gram serving of artichokeheart most fits the bill with:<br>

----------------------------------------
	Phosphorus: 0.36291 - (0.0456%)
	Potassium: 1.42202 - (0.0368%)
	protein: 14.37 - (0.0253%)
	Magnesium: 0.20883 - (0.0438%)
	Zinc: 0.00199 - (0.0159%)

----------------------------------------
	Vitamin K: 7.358e-05 - (0.0032% to max)
	Folate: 0.00044245 - (0.0389% to max)
	Manganese: 0.00112 - (0.0090% to max)
	Iron: 0.00304 - (0.0059% to max)
	Copper: 0.00063 - (0.0055% to max)
Additional Serving 3: Adding 44 grams of artichokeheart<br><br>

We seem to need these the most:  Vitamin A Potassium protein Magnesium Zinc<br>
But we need to avoid these:  Vitamin K Folate Manganese Iron Copper<br>
We think a 41 gram serving of corn most fits the bill with:<br>

----------------------------------------
	Vitamin A: 995 - (0.0272%)
	Potassium: 0.66 - (0.0159%)
	protein: 12.75 - (0.0209%)
	Magnesium: 0.14 - (0.0273%)
	Zinc: 0.00315 - (0.0235%)

----------------------------------------
	Vitamin K: 1.5e-06 - (0.0001% to max)
	Folate: 0.000175 - (0.0143% to max)
	Manganese: 0.00078 - (0.0058% to max)
	Iron: 0.00235 - (0.0043% to max)
	Copper: 0.00024 - (0.0020% to max)
Additional Serving 4: Adding 41 grams of corn<br><br>

We seem to need these the most:  B5 Potassium Magnesium protein Zinc<br>
But we need to avoid these:  Folate Vitamin K Manganese Iron Copper<br>
We think a 24 gram serving of mushrooms most fits the bill with:<br>

----------------------------------------
	B5: 0.00749 - (0.0719%)
	Potassium: 1.59 - (0.0224%)
	Magnesium: 0.045 - (0.0051%)
	protein: 15.45 - (0.0148%)
	Zinc: 0.0026 - (0.0113%)

----------------------------------------
	Folate: 8.5e-05 - (0.0041% to max)
	Vitamin K: 0 - (0.0000% to max)
	Manganese: 0.00024 - (0.0010% to max)
	Iron: 0.0025 - (0.0027% to max)
	Copper: 0.00159 - (0.0076% to max)
Additional Serving 5: Adding 24 grams of mushrooms<br><br>

We seem to need these the most:  Vitamin A Potassium protein Magnesium Zinc<br>
But we need to avoid these:  Folate Vitamin K Manganese Iron Copper<br>
We think a 39 gram serving of beets most fits the bill with:<br>

----------------------------------------
	Vitamin A: 175 - (0.0045%)
	Potassium: 1.525 - (0.0350%)
	protein: 8.4 - (0.0131%)
	Magnesium: 0.115 - (0.0214%)
	Zinc: 0.00175 - (0.0124%)

----------------------------------------
	Folate: 0.0004 - (0.0312% to max)
	Vitamin K: 1e-06 - (0.0000% to max)
	Manganese: 0.00163 - (0.0116% to max)
	Iron: 0.00395 - (0.0068% to max)
	Copper: 0.00037 - (0.0029% to max)
Additional Serving 6: Adding 39 grams of beets<br><br>

Nutrition Facts:<br>
	calories        552.016240000<br>
	carbs           46.173180000<br>
	*fiber           15.891920000 (41.82%) / (136.37%)<br>
	fat             38.432220000<br>
	monofat         20.082180000<br>
	polyfat         4.823460000<br>
	omega3          0.498300000 (31.14%) / (101.55%)<br>
	omega6          4.034100000 (23.73%) / (77.38%)<br>
	saturatedfat    5.298320000<br>
	*protein         14.017560000 (28.04%) / (91.42%)<br>
	B1              0.000237100 (19.76%) / (64.43%)<br>
	B2              0.000406400 (31.26%) / (101.94%)<br>
	B3              0.003888120 (24.30%) / (79.24%)<br>
	*B5              0.001857940 (37.16%) / (121.17%)<br>
	B6              0.000538360 (41.41%) / (135.04%)<br>
	B12             0.000000010 (0.40%) / (1.30%)<br>
	Biotin          0.000000000 (0.00%) / (0.00%)<br>
	Choline         0.086857760 (15.79%) / (51.50%)<br>
	*Folate          0.000248096 (62.02%) / (202.25%)<br>
	*Vitamin A       9312.427440000 (310.41%) / (1012.19%)<br>
	*Vitamin C       0.036653520 (40.73%) / (132.80%)<br>
	Vitamin D       1.680000000 (0.28%) / (0.91%)<br>
	Vitamin E       0.006748120 (44.99%) / (146.69%)<br>
	*Vitamin K       0.000314168 (261.81%) / (853.69%)<br>
	Calcium         0.149727920 (14.97%) / (48.82%)<br>
	Chromium        0.000000000 (0.00%) / (0.00%)<br>
	*Copper          0.000581500 (64.61%) / (210.68%)<br>
	Fluoride        0.000000000 (0.00%) / (0.00%)<br>
	Iodine          0.000000000 (0.00%) / (0.00%)<br>
	*Iron            0.003976120 (49.70%) / (162.07%)<br>
	*Magnesium       0.119597040 (28.48%) / (92.85%)<br>
	*Manganese       0.001327540 (57.72%) / (188.21%)<br>
	Molybdenum      0.000000000 (0.00%) / (0.00%)<br>
	*Phosphorus      0.268696080 (38.39%) / (125.17%)<br>
	*Potassium       1.134607760 (33.37%) / (108.81%)<br>
	Selenium        0.000008039 (14.62%) / (47.66%)<br>
	Sodium          0.219973920 (14.66%) / (47.82%)<br>
	*Zinc            0.001812150 (16.47%) / (53.72%)<br><br>
Ingredients to Add:<br>
	lettucegreen: 36 grams<br>
	lettucered: 36 grams<br>
	spinach: 30 grams<br>
	oliveoil: 27 grams<br>
	kidneybean: 44 grams<br>
	chickpeas: 41 grams<br>
	broccoli: 22 grams<br>
	mushrooms: 24 grams<br>
	artichokeheart: 44 grams<br>
	avacado: 57 grams<br>
	beets: 39 grams<br>
	corn: 41 grams<br>
	Total: 441
	
Bugs
====
It most definitley has alot of them.
