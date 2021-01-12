#Eureka! - Archimedes and King Hiero's Crown - www.101computing.net/eureka-and-king-hieros-crown/


mass = float(input("Input the mass of the crown in kg: "))
volume = float(input("Input the volume of the crown in cubic meter: "))

#Complete the code here to calculate the density and compare it with the density of a range of differen metals

density = mass/volume

print(f"Density is {density}")

if density > 2400 and density < 2700:
    print('The metal is Aluminium')

elif density > 8100 and density < 8300:
    print('The metal is Bronze')

elif density > 10400 and density < 10600:
    print('The metal is Silver')

elif density > 11200 and density < 11400:
    print('The metal is Lead')

elif density > 17100 and density < 17500:
    print("The metal is Gold")

elif density > 21000 and density < 21500:
    print('The metal is Platinum')

else:
    print('Unidentified metal')