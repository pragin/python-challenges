import constants


dailyCommute = constants.DISTANCE_BETWEEN_OXFORDTOLONDON * 2
weeklyCommute = dailyCommute * constants.WORKING_DAYS_PER_WEEK
yearlyCommute = weeklyCommute * constants.WEEKS_IN_YEAR
yearlyDistance = yearlyCommute * constants.KM_IN_MILE
moonTrip = constants.DISTANCE_BETWEEEN_EARTHANDMOON * 2
years = moonTrip / yearlyDistance


print(f'yuri would have travelled the equilant of going to the Moon and back in {years} years')