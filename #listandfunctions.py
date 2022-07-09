#creates class for vechicle- super class
class vehicle:
	def __init__(self,type):
	  #storing mechanism
		self.type=type 

#sub class for all other details
class automobile(vehicle):
	def __init__(self,type,year,make,model,doors,roof):
		super().__init__(type) #connecting to above super class
		self.year = year
		self.make = make
		self.model = model
		self.doors = doors
		self.roof = roof

type_i=input("Enter the type of vehicle :")
year_i=input("What year is it?")
make_i=input("Manufacture?")
model_i=input("Which model?")
doors_i=input("Is it a 2 or 4 door?")
roof_i=input("Solid roof or sun roof?")
A=automobile(type_i,year_i,make_i,model_i,doors_i,roof_i) # storing information

#print 
print("\nVehicle Type :"+A.type)#linking A to automobile to pull stored information for printing
print("\nYear :"+A.year)
print("\nMake :"+A.make)
print("\nModel :"+A.model)
print("\nNo of doors :"+A.doors)
print("\nType of roof :"+A.roof) 