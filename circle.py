import math 

radius = float(input("enter the radius of the circle: "))
area = math.pi * radius * radius
print("the area of the circle is:" ,area)


filename = input("Input the Filename: ")
f = filename.split(".")
print ("The extension of the file is : " + repr(f[-1]))
