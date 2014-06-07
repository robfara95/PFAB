class Animal(object):
	def __init__ (self,numberOfLegs, color, presenceOfFur, weight, length, species, name):
		self.numberOfLegs = numberOfLegs
		self.color = color
		self.presenceOfFur = presenceOfFur
		self.weight = weight
		self.length = length
		self.species = species
		self.name = name

	def sleep(self):
		print self.name, " the ", self.species, " is sleeping."

	def breathe(self):
		print self.name, " the ", self.species, " is breathing."

	def walk(self):
		print self.name, " the ", self.species, " is walking."

	def __str__(self):
		return "name: %s species: %s weight: %s length: %s num of legs: %s color: %s Prescence of Fur: %s" % (self.name, self.species, self.weight, self.length, self.numberOfLegs, self.color, self.presenceOfFur)

dog = Animal(4, "brown", "True", 24, 36, "canine", "Roofus")  
print dog
dog.sleep()
dog.breathe()
dog.walk()
cat = Animal(4, "grey", "True", 7, 27, "feline", "Mischief")
print cat
cat.sleep()
cat.breathe()
cat.walk()
