
# This program calculate how many lego bricks it would take to make the Earth out of lego bricks
# The following measurements are use
# Lego: width =16mm, length = 16mm, height = 10mm
# Earth: radius = 6371km
# Volume of a sphere = 4/3 * PI * r^3 

PI = 3.14
legoWidth = 16
legoLength = 16
legoHeight = 10
earthRadius = 6371 * 1000 * 100 * 10 # Converting 6371km to mm

print(f'Earth Radius {earthRadius}mm')

earthVolume = 4 * PI * (earthRadius**3 ) / 3
legoVolume =  legoHeight * legoLength * legoWidth

lego_needed = earthVolume/legoVolume
print(type(legoHeight))
print(type(legoLength))
print(type(legoWidth))
print(type(legoVolume))
print(type(earthRadius))
print(type(earthVolume))
print(f'earth Radius {earthRadius}')
print(f'earth volume {earthVolume}')
print(f'To build planet Earth out of Lego, we would need {lego_needed} lego bricks')

