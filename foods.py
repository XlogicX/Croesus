# Foods

# Food, each nutrient as per 500 grams. Everything measured in grams

targets_min = {
	"calories":0,
	"carbs":0,
	"fiber":38,
	"fat":0,
	"monofat":0,
	"polyfat":0,
	"omega3":1.6,
	"omega6":17,
	"saturatedfat":0,
	"protein":50,
	"B1":0.0012,
	"B2":0.0013,
	"B3":0.016,
	"B5":0.005,
	"B6": 0.0013,
	"B12":0.0000024,
	"Biotin":0.00003,
	"Choline":0.55,
	"Folate":0.0004,
	"Vitamin A":3000,
	"Vitamin C":0.09,
	"Vitamin D":600,
	"Vitamin E":0.015,
	"Vitamin K":0.00012,
	"Calcium":1,
	"Chromium":0.000035,
	"Copper":0.0009,
	"Fluoride":0.004,
	"Iodine":0.00015,
	"Iron":0.008,
	"Magnesium":0.42,
	"Manganese":0.0023,
	"Molybdenum":0.000045,
	"Phosphorus":0.7,
	"Potassium":3.4,
	"Selenium":0.000055,
	"Sodium":1.5,
	"Zinc":0.011
}

targets_max = {
	"calories":20000,
	"carbs":0,
	"fiber":0,
	"fat":0,
	"monofat":0,
	"polyfat":0,
	"omega3":0,
	"omega6":30,
	"saturatedfat":0,
	"protein":80,
	"B1":0,
	"B2":0,
	"B3":0.035,
	"B5":0,
	"B6": 0.1,
	"B12":0,
	"Biotin":0,
	"Choline":3.5,
	"Folate":0.001,
	"Vitamin A":0,
	"Vitamin C":2,
	"Vitamin D":4000,
	"Vitamin E":1,
	"Vitamin K":0.002,
	"Calcium":2.5,
	"Chromium":0,
	"Copper":0.01,
	"Fluoride":0.01,
	"Iodine":0.0011,
	"Iron":0.045,
	"Magnesium":0,
	"Manganese":0.011,
	"Molybdenum":0.002,
	"Phosphorus":4,
	"Potassium":0,
	"Selenium":0.0004,
	"Sodium":2.3,
	"Zinc":0.04
}

food = {
	# Legumes
	"blackbean":{
		"calories":700,
		"carbs":130.25,
		"fiber":52.5,
		"fat":3.1,
		"monofat":0.71,
		"polyfat":2.45,
		"omega3":0.89,
		"omega6":0.68,
		"saturatedfat":0.49,
		"protein":41.15,
		"B1":0.00119,
		"B2":0.00033,
		"B3":0.00325,
		"B5":0.00133,
		"B6": 0.00069,
		"B12":0,
		"Biotin":0,
		"Choline":0.2235,
		"Folate":0.0007,
		"Vitamin A":0,
		"Vitamin C":0.0045,
		"Vitamin D":0,
		"Vitamin E":0.00005,
		"Vitamin K":0.000003,
		"Calcium":0.345,
		"Chromium":0,
		"Copper":0.00105,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0118,
		"Magnesium":0.265,
		"Manganese":0.00264,
		"Molybdenum":0,
		"Phosphorus":0.72,
		"Potassium":1.945,
		"Selenium":0.0000145,
		"Sodium":0,
		"Zinc":0.00515},
	"kidneybean":{
		"calories":620,
		"carbs":107.45,
		"fiber":27.5,
		"fat":5.25,
		"monofat":0.15,
		"polyfat":0.97,
		"omega3":0.29,
		"omega6":0.6,
		"saturatedfat":0.91,
		"protein":39.9,
		"B1":0.00034,
		"B2":0.00008,
		"B3":0.0023,
		"B5":0.00104,
		"B6":0.00057,
		"B12":0,
		"Biotin":0,
		"Choline":0.1435,
		"Folate":0.000140,
		"Vitamin A":0,
		"Vitamin C":0.001,
		"Vitamin D":0,
		"Vitamin E":0.00014,
		"Vitamin K":0.0000395,
		"Calcium":0.285,
		"Chromium":0,
		"Copper":0.00136,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0075,
		"Magnesium":0.15,
		"Manganese":0.00192,
		"Molybdenum":0,
		"Phosphorus":0.605,
		"Potassium":1.385,
		"Selenium":0.000008,
		"Sodium":0.005,
		"Zinc":0.00375},
	"pintobean":{
		"calories":570,
		"carbs":101.1,
		"fiber":27.5,
		"fat":4.5,
		"monofat":0.77,
		"polyfat":1.37,
		"omega3":0.79,
		"omega6":0.58,
		"saturatedfat":0.79,
		"protein":34.95,
		"B1":0.00026,
		"B2":0.0001,
		"B3":0.00136,
		"B5":0.00082,
		"B6":0.00089,
		"B12":0,
		"Biotin":0,
		"Choline":0.137,
		"Folate":0.000120,
		"Vitamin A":0,
		"Vitamin C":0.0005,
		"Vitamin D":0,
		"Vitamin E":0.00365,
		"Vitamin K":0.0000135,
		"Calcium":0.315,
		"Chromium":0,
		"Copper":0.0013,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00665,
		"Magnesium":0.160,
		"Manganese":0.00192,
		"Molybdenum":0,
		"Phosphorus":0.505,
		"Potassium":1.370,
		"Selenium":0.000024,
		"Sodium":0.005,
		"Zinc":0.00305},
	"chickpeas":{
		"calories":695,
		"carbs":112.65,
		"fiber":32,
		"fat":13.85,
		"monofat":2.44,
		"polyfat":4.84,
		"omega3":0.18,
		"omega6":3.74,
		"saturatedfat":1.07,
		"protein":35.25,
		"B1":0.00014,
		"B2":0.00008,
		"B3":0.0007,
		"B5":0.0012,
		"B6":0.00058,
		"B12":0,
		"Biotin":0,
		"Choline":0.179,
		"Folate":0.000240,
		"Vitamin A":115,
		"Vitamin C":0.0005,
		"Vitamin D":0,
		"Vitamin E":0.00145,
		"Vitamin K":0.000017,
		"Calcium":0.225,
		"Chromium":0,
		"Copper":0.00127,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00535,
		"Magnesium":0.13,
		"Manganese":0.00423,
		"Molybdenum":0,
		"Phosphorus":0.425,
		"Potassium":0.63,
		"Selenium":0.0000155,
		"Sodium":0.035,
		"Zinc":0.000315},											

	# Vegetables (spinach is from frozen)
	"redonion":{
		"calories":200,
		"carbs":46.7,
		"fiber":7.3,
		"fat":0.5,
		"monofat":0.07,
		"polyfat":0.09,
		"omega3":0.02,
		"omega6":0,
		"saturatedfat":0.21,
		"protein":5.5,
		"B1":0.00023,
		"B2":0.00014,
		"B3":0.00058,
		"B5":0.00062,
		"B6":0.0006,
		"B12":0,
		"Biotin":0,
		"Choline":0.0305,
		"Folate":0.000095,
		"Vitamin A":10,
		"Vitamin C":0.037,
		"Vitamin D":0,
		"Vitamin E":0.0001,
		"Vitamin K":0.000002,
		"Calcium":0.115,
		"Chromium":0,
		"Copper":0.0002,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.000105,
		"Magnesium":0.05,
		"Manganese":0.00065,
		"Molybdenum":0,
		"Phosphorus":0.145,
		"Potassium":0.730,
		"Selenium":0.0000025,
		"Sodium":0.02,
		"Zinc":0.00085},
	"redbellpepper":{
		"calories":130,
		"carbs":30.15,
		"fiber":10.5,
		"fat":1.5,
		"monofat":0.04,
		"polyfat":0.78,
		"omega3":0.28,
		"omega6":0,
		"saturatedfat":0.3,
		"protein":4.95,
		"B1":0.00027,
		"B2":0.00043,
		"B3":0.0049,
		"B5":0.00159,
		"B6":0.00146,
		"B12":0,
		"Biotin":0,
		"Choline":0.028,
		"Folate":0.000230,
		"Vitamin A":15655,
		"Vitamin C":0.6385,
		"Vitamin D":0,
		"Vitamin E":0.0079,
		"Vitamin K":0.0000245,
		"Calcium":0.035,
		"Chromium":0,
		"Copper":0.00009,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00215,
		"Magnesium":0.06,
		"Manganese":0.00056,
		"Molybdenum":0,
		"Phosphorus":0.130,
		"Potassium":1.055,
		"Selenium":0.0000005,
		"Sodium":0.02,
		"Zinc":0.00125},
	"corn":{
		"calories":405,
		"carbs":96.5,
		"fiber":12,
		"fat":3.35,
		"monofat":0.99,
		"polyfat":1.59,
		"omega3":0.05,
		"omega6":0.46,
		"saturatedfat":0.52,
		"protein":12.75,
		"B1":0.00015,
		"B2":0.00031,
		"B3":0.00656,
		"B5":0.00076,
		"B6":0.0005,
		"B12":0,
		"Biotin":0,
		"Choline":0.11,
		"Folate":0.000175,
		"Vitamin A":995,
		"Vitamin C":0.0175,
		"Vitamin D":0,
		"Vitamin E":0.00035,
		"Vitamin K":0.0000015,
		"Calcium":0.015,
		"Chromium":0,
		"Copper":0.00024,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00235,
		"Magnesium":0.140,
		"Manganese":0.00078,
		"Molybdenum":0,
		"Phosphorus":0.395,
		"Potassium":0.66,
		"Selenium":0.0000035,
		"Sodium":0.005,
		"Zinc":0.00315},
	"greenbellpepper":{
		"calories":100,
		"carbs":23.2,
		"fiber":8.5,
		"fat":0.85,
		"monofat":0.04,
		"polyfat":0.31,
		"omega3":0.04,
		"omega6":0,
		"saturatedfat":0.29,
		"protein":4.3,
		"B1":0.00029,
		"B2":0.00014,
		"B3":0.0024,
		"B5":0.0005,
		"B6":0.00112,
		"B12":0,
		"Biotin":0,
		"Choline":0.0275,
		"Folate":0.00005,
		"Vitamin A":1850,
		"Vitamin C":0.402,
		"Vitamin D":0,
		"Vitamin E":0.0004,
		"Vitamin K":0.0000355,
		"Calcium":0.05,
		"Chromium":0,
		"Copper":0.00033,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0017,
		"Magnesium":0.05,
		"Manganese":0.00061,
		"Molybdenum":0,
		"Phosphorus":0.1,
		"Potassium":0.875,
		"Selenium":0,
		"Sodium":0.015,
		"Zinc":0.00065},
	"crushedtomato":{
		"calories":160,
		"carbs":36.45,
		"fiber":9.5,
		"fat":1.4,
		"monofat":0.22,
		"polyfat":0.57,
		"omega3":0.03,
		"omega6":0.54,
		"saturatedfat":0.2,
		"protein":8.2,
		"B1":0.00038,
		"B2":0.00026,
		"B3":0.00611,
		"B5":0.00139,
		"B6":0.00075,
		"B12":0,
		"Biotin":0,
		"Choline":0.0645,
		"Folate":0.000065,
		"Vitamin A":1075,
		"Vitamin C":0.046,
		"Vitamin D":0,
		"Vitamin E":0.00625,
		"Vitamin K":0.0000265,
		"Calcium":0.170,
		"Chromium":0,
		"Copper":0.00092,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0065,
		"Magnesium":0.1,
		"Manganese":0.00092,
		"Molybdenum":0,
		"Phosphorus":0.160,
		"Potassium":1.465,
		"Selenium":0.000003,
		"Sodium":0.93,
		"Zinc":0.00135},
	"zuchini":{
		"calories":85,
		"carbs":15.55,
		"fiber":5,
		"fat":1.6,
		"monofat":0.06,
		"polyfat":0.46,
		"omega3":0.31,
		"omega6":0.15,
		"saturatedfat":0.42,
		"protein":6.05,
		"B1":0.00023,
		"B2":0.00047,
		"B3":0.00226,
		"B5":0.00102,
		"B6":0.00082,
		"B12":0,
		"Biotin":0,
		"Choline":0.0475,
		"Folate":0.00012,
		"Vitamin A":1000,
		"Vitamin C":0.0895,
		"Vitamin D":0,
		"Vitamin E":0.0006,
		"Vitamin K":0.0000215,
		"Calcium":0.08,
		"Chromium":0,
		"Copper":0.00027,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00185,
		"Magnesium":0.09,
		"Manganese":0.00089,
		"Molybdenum":0,
		"Phosphorus":0.190,
		"Potassium":1.305,
		"Selenium":0.000001,
		"Sodium":0.04,
		"Zinc":0.0016},
	"cauliflour":{
		"calories":125,
		"carbs":24.85,
		"fiber":10,
		"fat":1.4,
		"monofat":0.17,
		"polyfat":0.16,
		"omega3":0.08,
		"omega6":0.07,
		"saturatedfat":0.65,
		"protein":9.6,
		"B1":0.00025,
		"B2":0.0003,
		"B3":0.00254,
		"B5":0.00334,
		"B6":0.00092,
		"B12":0,
		"Biotin":0,
		"Choline":0.2215,
		"Folate":0.000285,
		"Vitamin A":0,
		"Vitamin C":0.241,
		"Vitamin D":0,
		"Vitamin E":0.0004,
		"Vitamin K":0.0000775,
		"Calcium":0.11,
		"Chromium":0,
		"Copper":0.0002,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0021,
		"Magnesium":0.075,
		"Manganese":0.00078,
		"Molybdenum":0,
		"Phosphorus":0.22,
		"Potassium":1.495,
		"Selenium":0.000003,
		"Sodium":0.150,
		"Zinc":0.00135},
	"broccoli":{
		"calories":170,
		"carbs":33.2,
		"fiber":13,
		"fat":1.85,
		"monofat":0.16,
		"polyfat":0.56,
		"omega3":0.32,
		"omega6":0,
		"saturatedfat":0.57,
		"protein":14.1,
		"B1":0.00036,
		"B2":0.00059,
		"B3":0.0032,
		"B5":0.00287,
		"B6":0.00088,
		"B12":0,
		"Biotin":0,
		"Choline":0.0935,
		"Folate":0.000315,
		"Vitamin A":3115,
		"Vitamin C":0.446,
		"Vitamin D":0,
		"Vitamin E":0.0072,
		"Vitamin K":0.00051,
		"Calcium":0.235,
		"Chromium":0,
		"Copper":0.00025,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00365,
		"Magnesium":0.105,
		"Manganese":0.00105,
		"Molybdenum":0,
		"Phosphorus":0.33,
		"Potassium":1.580,
		"Selenium":0.0000125,
		"Sodium":0.165,
		"Zinc":0.00205},
	"carrots":{
		"calories":205,
		"carbs":47.9,
		"fiber":14,
		"fat":1.2,
		"monofat":0.06,
		"polyfat":0.51,
		"omega3":0.01,
		"omega6":0,
		"saturatedfat":0.16,
		"protein":4.65,
		"B1":0.00033,
		"B2":0.00029,
		"B3":0.00492,
		"B5":0.00137,
		"B6":0.00069,
		"B12":0,
		"Biotin":0,
		"Choline":0.044,
		"Folate":0.000095,
		"Vitamin A":83530,
		"Vitamin C":0.0295,
		"Vitamin D":0,
		"Vitamin E":0.0043,
		"Vitamin K":0.0000415,
		"Calcium":0.165,
		"Chromium":0,
		"Copper":0.00023,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0015,
		"Magnesium":0.06,
		"Manganese":0.00072,
		"Molybdenum":0,
		"Phosphorus":0.175,
		"Potassium":1.6,
		"Selenium":0.0000005,
		"Sodium":0.345,
		"Zinc":0.0012},
	"spinach":{
		"calories":170,
		"carbs":24,
		"fiber":18.5,
		"fat":4.35,
		"monofat":0,
		"polyfat":1.86,
		"omega3":1.86,
		"omega6":0,
		"saturatedfat":0.79,
		"protein":20.05,
		"B1":0.00039,
		"B2":0.00088,
		"B3":0.0022,
		"B5":0.00038,
		"B6":0.00068,
		"B12":0,
		"Biotin":0,
		"Choline":0.124,
		"Folate":0.000605,
		"Vitamin A":60305,
		"Vitamin C":0.011,
		"Vitamin D":0,
		"Vitamin E":0.0177,
		"Vitamin K":0.0027035,
		"Calcium":0.765,
		"Chromium":0,
		"Copper":0.00081,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0098,
		"Magnesium":0.41,
		"Manganese":0.00359,
		"Molybdenum":0,
		"Phosphorus":0.250,
		"Potassium":1.51,
		"Selenium":0.0000275,
		"Sodium":0.485,
		"Zinc":0.00245},
	"olives":{
		"calories":580,
		"carbs":30.2,
		"fiber":8,
		"fat":54.5,
		"monofat":38.6,
		"polyfat":3.15,
		"omega3":0,
		"omega6":3.15,
		"saturatedfat":11.4,
		"protein":4.2,
		"B1":0.00002,
		"B2":0,
		"B3":0.00019,
		"B5":0.00008,
		"B6":0.00005,
		"B12":0,
		"Biotin":0,
		"Choline":0.0515,
		"Folate":0,
		"Vitamin A":1650,
		"Vitamin C":0.0045,
		"Vitamin D":0,
		"Vitamin E":0.00825,
		"Vitamin K":0.000007,
		"Calcium":0.44,
		"Chromium":0,
		"Copper":0.00126,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0314,
		"Magnesium":0.02,
		"Manganese":0.0001,
		"Molybdenum":0,
		"Phosphorus":0.015,
		"Potassium":0.04,
		"Selenium":0.0000045,
		"Sodium":3.675,
		"Zinc":0.0011},
	"olivesgreen":{
		"calories":725,
		"carbs":19.2,
		"fiber":16.5,
		"fat":76.6,
		"monofat":56.57,
		"polyfat":6.54,
		"omega3":0.46,
		"omega6":6.08,
		"saturatedfat":10.15,
		"protein":5.15,
		"B1":0.00011,
		"B2":0.00004,
		"B3":0.00119,
		"B5":0.00012,
		"B6":0.00016,
		"B12":0,
		"Biotin":0,
		"Choline":0.071,
		"Folate":0.000015,
		"Vitamin A":1965,
		"Vitamin C":0,
		"Vitamin D":0,
		"Vitamin E":0.001905,
		"Vitamin K":0.000007,
		"Calcium":0.26,
		"Chromium":0,
		"Copper":0.0006,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00245,
		"Magnesium":0.055,
		"Manganese":0.0001,
		"Molybdenum":0,
		"Phosphorus":0.02,
		"Potassium":0.210,
		"Selenium":0.0000045,
		"Sodium":7.78,
		"Zinc":0.0002},
	"peas":{
		"calories":390,
		"carbs":71.3,
		"fiber":22.5,
		"fat":1.35,
		"monofat":0.12,
		"polyfat":0.65,
		"omega3":0.12,
		"omega6":0,
		"saturatedfat":0.25,
		"protein":25.75,
		"B1":0.00142,
		"B2":0.0005,
		"B3":0.0074,
		"B5":0.00071,
		"B6":0.00057,
		"B12":0,
		"Biotin":0,
		"Choline":0.1375,
		"Folate":0.000295,
		"Vitamin A":10500,
		"Vitamin C":0.0495,
		"Vitamin D":0,
		"Vitamin E":0.00015,
		"Vitamin K":0.00012,
		"Calcium":0.120,
		"Chromium":0,
		"Copper":0.00053,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0076,
		"Magnesium":0.11,
		"Manganese":0.0014,
		"Molybdenum":0,
		"Phosphorus":0.385,
		"Potassium":0.55,
		"Selenium":0.000005,
		"Sodium":0.36,
		"Zinc":0.00335},
	"lettucegreen":{
		"calories":75,
		"carbs":14.35,
		"fiber":6.5,
		"fat":0.75,
		"monofat":0.03,
		"polyfat":0.41,
		"omega3":0.29,
		"omega6":0,
		"saturatedfat":0.1,
		"protein":6.8,
		"B1":0.00035,
		"B2":0.0004,
		"B3":0.00188,
		"B5":0.00067,
		"B6":0.00045,
		"B12":0,
		"Biotin":0,
		"Choline":0.068,
		"Folate":0.000190,
		"Vitamin A":37025,
		"Vitamin C":0.046,
		"Vitamin D":0,
		"Vitamin E":0.0011,
		"Vitamin K":0.0006315,
		"Calcium":0.180,
		"Chromium":0,
		"Copper":0.00015,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0043,
		"Magnesium":0.065,
		"Manganese":0.00125,
		"Molybdenum":0,
		"Phosphorus":0.145,
		"Potassium":0.97,
		"Selenium":0.000003,
		"Sodium":0.140,
		"Zinc":0.0009},
	"lettucered":{
		"calories":65,
		"carbs":11.3,
		"fiber":4.5,
		"fat":1.1,
		"monofat":0.05,
		"polyfat":0.58,
		"omega3":0.26,
		"omega6":0,
		"saturatedfat":0.14,
		"protein":6.65,
		"B1":0.00032,
		"B2":0.00039,
		"B3":0.00161,
		"B5":0.00072,
		"B6":0.0005,
		"B12":0,
		"Biotin":0,
		"Choline":0.059,
		"Folate":0.00018,
		"Vitamin A":37460,
		"Vitamin C":0.0185,
		"Vitamin D":0,
		"Vitamin E":0.00075,
		"Vitamin K":0.000615,
		"Calcium":0.165,
		"Chromium":0,
		"Copper":0.00014,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.006,
		"Magnesium":0.06,
		"Manganese":0.00102,
		"Molybdenum":0,
		"Phosphorus":0.140,
		"Potassium":0.935,
		"Selenium":0.0000075,
		"Sodium":0.125,
		"Zinc":0.001},
	"artichokeheart":{
		"calories":263.48,
		"carbs":59.41,
		"fiber":28.34,
		"fat":1.69,
		"monofat":0.06,
		"polyfat":0.72,
		"omega3":0.19,
		"omega6":0,
		"saturatedfat":0.4,
		"protein":14.37,
		"B1":0.00025,
		"B2":0.00044,
		"B3":0.00552,
		"B5":0.0012,
		"B6":0.00041,
		"B12":0,
		"Biotin":0,
		"Choline":0.17102,
		"Folate":0.00044245,
		"Vitamin A":64.63,
		"Vitamin C":0.03679,
		"Vitamin D":0,
		"Vitamin E":0.00095,
		"Vitamin K":0.00007358,
		"Calcium":0.10509,
		"Chromium":0,
		"Copper":0.00063,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00304,
		"Magnesium":0.20883,
		"Manganese":0.00112,
		"Molybdenum":0,
		"Phosphorus":0.36291,
		"Potassium":1.42202,
		"Selenium":0.000001,
		"Sodium":1.41459,
		"Zinc":0.00199},
	"cucumber":{
		"calories":75,
		"carbs":18.15,
		"fiber":5.7,
		"fat":0.55,
		"monofat":0.03,
		"polyfat":0.16,
		"omega3":0.03,
		"omega6":0.14,
		"saturatedfat":0.19,
		"protein":3.25,
		"B1":0.00014,
		"B2":0.00017,
		"B3":0.00049,
		"B5":0.0013,
		"B6":0.0002,
		"B12":0,
		"Biotin":0,
		"Choline":0.03,
		"Folate":0.000035,
		"Vitamin A":525,
		"Vitamin C":0.014,
		"Vitamin D":0,
		"Vitamin E":0.00015,
		"Vitamin K":0.000082,
		"Calcium":0.08,
		"Chromium":0,
		"Copper":0.00021,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0014,
		"Magnesium":0.065,
		"Manganese":0.0004,
		"Molybdenum":0,
		"Phosphorus":0.12,
		"Potassium":0.735,
		"Selenium":0.0000015,
		"Sodium":0.01,
		"Zinc":0.001},
	"beets":{
		"calories":220,
		"carbs":49.8,
		"fiber":10,
		"fat":0.9,
		"monofat":0.18,
		"polyfat":0.32,
		"omega3":0.03,
		"omega6":0,
		"saturatedfat":0.14,
		"protein":8.4,
		"B1":0.00014,
		"B2":0.0002,
		"B3":0.0016,
		"B5":0.00073,
		"B6":0.00034,
		"B12":0,
		"Biotin":0,
		"Choline":0.0315,
		"Folate":0.0004,
		"Vitamin A":175,
		"Vitamin C":0.018,
		"Vitamin D":0,
		"Vitamin E":0.0002,
		"Vitamin K":0.000001,
		"Calcium":0.08,
		"Chromium":0,
		"Copper":0.00037,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00395,
		"Magnesium":0.115,
		"Manganese":0.00163,
		"Molybdenum":0,
		"Phosphorus":0.19,
		"Potassium":1.525,
		"Selenium":0.0000035,
		"Sodium":0.385,
		"Zinc":0.00175},

	# Seasonings/Spices
	"garlic":{
		"calories":745,
		"carbs":165.3,
		"fiber":10.5,
		"fat":2.5,
		"monofat":0.09,
		"polyfat":1.25,
		"omega3":0.1,
		"omega6":1.12,
		"saturatedfat":0.47,
		"protein":31.8,
		"B1":0.001,
		"B2":0.00055,
		"B3":0.0035,
		"B5":0.00298,
		"B6":0.00618,
		"B12":0,
		"Biotin":0,
		"Choline":0.116,
		"Folate":0.000015,
		"Vitamin A":45,
		"Vitamin C":0.156,
		"Vitamin D":0,
		"Vitamin E":0.0004,
		"Vitamin K":0.0000085,
		"Calcium":0.905,
		"Chromium":0,
		"Copper":0.0015,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0085,
		"Magnesium":0.125,
		"Manganese":0.00836,
		"Molybdenum":0,
		"Phosphorus":0.765,
		"Potassium":2.005,
		"Selenium":0.000071,
		"Sodium":0.085,
		"Zinc":0.0058},
	"iodizedsalt":{
		"calories":0,
		"carbs":0,
		"fiber":0,
		"fat":0,
		"monofat":0,
		"polyfat":0,
		"omega3":0,
		"omega6":0,
		"saturatedfat":0,
		"protein":0,
		"B1":0,
		"B2":0,
		"B3":0,
		"B5":0,
		"B6":0,
		"B12":0,
		"Biotin":0,
		"Choline":0,
		"Folate":0,
		"Vitamin A":0,
		"Vitamin C":0,
		"Vitamin D":0,
		"Vitamin E":0,
		"Vitamin K":0,
		"Calcium":0.12,
		"Chromium":0,
		"Copper":0.00015,
		"Fluoride":0,
		"Iodine":0.022,
		"Iron":0.0016,
		"Magnesium":0.005,
		"Manganese":0.0005,
		"Molybdenum":0,
		"Phosphorus":0,
		"Potassium":0.04,
		"Selenium":0.0000005,
		"Sodium":193.79,
		"Zinc":0.0005},
	"cocoapowder":{
		"calories":1140,
		"carbs":289.5,
		"fiber":185,
		"fat":68.5,
		"monofat":22.85,
		"polyfat":2.2,
		"omega3":0,
		"omega6":2.2,
		"saturatedfat":40.35,
		"protein":98,
		"B1":0.00039,
		"B2":0.00121,
		"B3":0.01093,
		"B5":0.00127,
		"B6":0.00059,
		"B12":0,
		"Biotin":0,
		"Choline":0.06,
		"Folate":0.00016,
		"Vitamin A":0,
		"Vitamin C":0,
		"Vitamin D":0,
		"Vitamin E":0.0005,
		"Vitamin K":0.0000125,
		"Calcium":0.64,
		"Chromium":0,
		"Copper":0.01894,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0693,
		"Magnesium":2.495,
		"Manganese":0.01919,
		"Molybdenum":0,
		"Phosphorus":3.67,
		"Potassium":7.62,
		"Selenium":0.0000715,
		"Sodium":0.105,
		"Zinc":0.03405},

	# Oils
	"oliveoil":{
		"calories":4420,
		"carbs":0,
		"fiber":0,
		"fat":500,
		"monofat":364.81,
		"polyfat":52.62,
		"omega3":3.81,
		"omega6":48.8,
		"saturatedfat":69.04,
		"protein":0,
		"B1":0,
		"B2":0,
		"B3":0,
		"B5":0,
		"B6":0,
		"B12":0,
		"Biotin":0,
		"Choline":0.0015,
		"Folate":0,
		"Vitamin A":0,
		"Vitamin C":0,
		"Vitamin D":0,
		"Vitamin E":0.07175,
		"Vitamin K":0.000301,
		"Calcium":0.005,
		"Chromium":0,
		"Copper":0,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0028,
		"Magnesium":0,
		"Manganese":0,
		"Molybdenum":0,
		"Phosphorus":0,
		"Potassium":0.005,
		"Selenium":0,
		"Sodium":0.01,
		"Zinc":0},

	# Grains

	# Berries

	# Other Fruits
	"tomato":{
		"calories":90,
		"carbs":19.45,
		"fiber":6,
		"fat":1,
		"monofat":0.16,
		"polyfat":0.42,
		"omega3":0.02,
		"omega6":0,
		"saturatedfat":0.14,
		"protein":4.4,
		"B1":0.00019,
		"B2":0.0001,
		"B3":0.00297,
		"B5":0.00045,
		"B6":0.0004,
		"B12":0,
		"Biotin":0,
		"Choline":0.0335,
		"Folate":0.000075,
		"Vitamin A":4165,
		"Vitamin C":0.0685,
		"Vitamin D":0,
		"Vitamin E":0.0027,
		"Vitamin K":0.0000395,
		"Calcium":0.05,
		"Chromium":0,
		"Copper":0.0003,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00135,
		"Magnesium":0.055,
		"Manganese":0.00057,
		"Molybdenum":0,
		"Phosphorus":0.120,
		"Potassium":1.185,
		"Selenium":0,
		"Sodium":0.025,
		"Zinc":0.00085},
	"avacado":{
		"calories":835,
		"carbs":43.2,
		"fiber":34,
		"fat":77.05,
		"monofat":0.49,
		"polyfat":9.08,
		"omega3":0.56,
		"omega6":8.45,
		"saturatedfat":10.63,
		"protein":9.8,
		"B1":0.00038,
		"B2":0.00071,
		"B3":0.00956,
		"B5":0.00732,
		"B6":0.00144,
		"B12":0,
		"Biotin":0,
		"Choline":0.071,
		"Folate":0.000445,
		"Vitamin A":735,
		"Vitamin C":0.044,
		"Vitamin D":0,
		"Vitamin E":0.00965,
		"Vitamin K":0.000105,
		"Calcium":0.065,
		"Chromium":0,
		"Copper":0.00085,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.00305,
		"Magnesium":0.145,
		"Manganese":0.00075,
		"Molybdenum":0,
		"Phosphorus":0.270,
		"Potassium":2.535,
		"Selenium":0.000002,
		"Sodium":0.04,
		"Zinc":0.0034},

	# Nuts/Seeds

	# Other
	"mushrooms":{
		"calories":110,
		"carbs":16.3,
		"fiber":5,
		"fat":1.7,
		"monofat":0,
		"polyfat":0.8,
		"omega3":0,
		"omega6":0.8,
		"saturatedfat":0.25,
		"protein":15.45,
		"B1":0.00041,
		"B2":0.00201,
		"B3":0.01804,
		"B5":0.00749,
		"B6":0.00052,
		"B12":0.0000002,
		"Biotin":0,
		"Choline":0.0865,
		"Folate":0.000085,
		"Vitamin A":0,
		"Vitamin C":0.0105,
		"Vitamin D":35,
		"Vitamin E":0.00005,
		"Vitamin K":0,
		"Calcium":0.015,
		"Chromium":0,
		"Copper":0.00159,
		"Fluoride":0,
		"Iodine":0,
		"Iron":0.0025,
		"Magnesium":0.045,
		"Manganese":0.00024,
		"Molybdenum":0,
		"Phosphorus":0.43,
		"Potassium":1.59,
		"Selenium":0.0000465,
		"Sodium":0.025,
		"Zinc":0.0026},

}


#pepper
#tbsp chili powder
#tsp cumin
#tsp corriander
#tsp garlic powder
#1/4 tsp cyan
#splash of soy sauce
#turmeric
#chili peppers?