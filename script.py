import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

average_calories = np.mean(calorie_stats)
print average_calories

calorie_stats_sorted = np.sort(calorie_stats)
print calorie_stats_sorted

median_calories = np.median(calorie_stats)
print median_calories

first_quartile = np.percentile(calorie_stats, 25)
third_quartile = np.percentile(calorie_stats, 75)
print first_quartile
print third_quartile

nth_percentile = first_quartile
print nth_percentile

more_calories = np.mean(calorie_stats > 60)
print more_calories

calorie_std = np.std(calorie_stats)
print calorie_std

summery = ('From this data, we know that CrunchieMunchies is in the 4th percentile of all cereals on the market, with other cereals being 96% more caloric than CrunchieMunchies. We also know that the standard deviation is low.')
print summery



