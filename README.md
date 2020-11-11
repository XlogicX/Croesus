Takes your ingredient suggestions and crafts a recipe (portions) that attempts to maximize on nutrition

Usage
====
nutrition_balancer.py [-h] [-r R] [-d [D]] [-o [O]] [-s [S]] [-b B]

Nutritionally Balanced Ingredient Ratios based on general recipe suggestions

optional arguments:
  -h, --help  show this help message and exit
  -r R        Recipe File
  -d [D]      Debug - Tells you what the program is thinking
  -o [O]      Override Nutrient goals with the one in recipe file
  -s [S]      Suggest target nutrients (like override), but allow program to
              still eliminate nutrients in your suggestion that aren't
              practical
  -b B        Ammount of nutrients to back off on

Configuration Files
====
First, we need a file that has a list of all available foods that we normally expect to by at our own grocery, not exotic shit that we don't. This file also lists the minimum RDI value of each nutrient, and if applicable, the level at which that nutrient becomes toxic. The foods themselves are likely accurate enough, but these RDI values can actually be very individual, based on gender, age, and other things. The sample file in this git is foods.py

Next, we need our actual recipe file, it can be named anything, but it does need to be in json format. First is every ingredient, with a key for minimum, maximum, and serving size (called resolution). Everything is measured in grams. I know its not flexible, and probably not super accurate for fluid measurements, just deal with it. You can use these values to stress that a food is optional (min = 0) or has a required amount (min=required ammount). You can use the 'max' value to set a cap on each ingredient (kale and spinach are healthy, but...). Finally, 'res' is for the serving size; how many means or olives come in one can or something like that. But if your pouring frozen corn out of a back, fuckit, set 'res' to 1 (1 gram), It's cool to see super granular proportions.

Below the foods, we also set a cap for weight, calories, and servings, this is how the program knows when to stop adding food. Weight is a cludgy substitute for volume, I focus on this limit for something like a chili recipe (put in enough food to fill to pot, calories and servings be damned). I like using servings for a situation where I'm ordering something like a salad online, and can pick up to (lets say) 8 ingredients. You can also have the program stop at a specific calorie limit as well.

How It Works
====
Tediously, in no way will I say any of this is convenient. This script was just for me, but why not make it public anyway.

The TL;DR is that it incrementally keeps adding servings of your foods defined in a recipe file based on which food best satisfies the demanded nutrient profile.

That's an oversimplification obviously.

First, before it does anything worth thinking about, it considers all of the foods in your recipe that have minimum required ammounts and adds them without thought, because that is what you demanded by putting those minimums in your recipe file.

Also before getting into a loop on adding additional servings, it will preprocess what nutrients it things are going to be the most practical to target; to play to the strengths of the ingredients in the recipe. In other words, what fucking sense does it make to look at a list of vegetables, see that our meal is currently lacking in vitamin B12, and keep trying to add foods that have the most of that. The rest of the vitamins and minerals that vegegtables play well to might get neglected (or more likely, off balance).

The nutrient preprocessing is attacked from a couple of angles. One way to look at it is to just fill up the whole back with the maximum ammounts (as defined in our recipe file) of each food, and to see if we can even acheive 100% or more rdi of any of the nutrients. Another way is to look at each food, and see if we hypothetically ate our daily calorie limit in just that food, which nutrients can we get to 100% or more on. The preprocessing considers both of these methods.

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

The recipe I end up with is:
Ingredients to Add:
	lettucegreen: 36 grams
	lettucered: 36 grams
	spinach: 30 grams
	oliveoil: 27 grams
	chickpeas: 41 grams
	redonion: 48 grams
	broccoli: 22 grams
	olives: 40 grams
	olivesgreen: 40 grams
	mushrooms: 24 grams
	beets: 39 grams
	corn: 41 grams
	Total: 424

It is slightly different than the salad I always ordered before this one, and is nutritionally better consistently down the line compared to it. Though, it's marginally better; like 10%-50% increases for each nutrient, but usually around the 10% range for most. I guess this didn't surprise me, so long as all the ingredients I'm throwing into the bowl are healthy veggies and healthy whole foods, it's kind of hard to fuck up. But why not squeeze that extra 10% of efficiency out of the calories consumed?

Bugs
====
It most definitley has alot of them.
