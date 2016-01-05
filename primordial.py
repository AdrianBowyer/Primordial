# 1 Dimensional evolutionary model
# Adrian Bowyer
# January 2016

sizeEnergy = 1.0

#---------------------------------------------------------
# An individual has one phenotype

class Phenotype:
 size = 1.0

#---------------------------------------------------------
# An individual has a collection of genes

class Gene:
 
#---------------------------------------------------------
# An individual organism

class Individual:
 genes = []
 Phenotype phenotype
 position = 0.0
 speed = 0.0
 age = 0.0
 energy = 1.0

 def tick():
  age = age + 1.0
  position = position + speed
  energy = energy - speed*speed

 def save(worldFile):


 def load(worldFile):

#---------------------------------------------------------
# All the organisms and their 1D world

class World
 individuals = []
 time = 0.0

 def tick():
  for individual in individuals
   individual.tick()
  time = time + 1.0

 def save(fileName):
  worldFile = file(fileName)
  worldFile.write(str(time) + "\n")
  for individual in individuals
   individual.save(worldFile)

 def load(fileName):
  worldFile = file(fileName)
  time = float(worldFile.readline())
  while True:
   i = Individual.load(worldFile)
   if i is None:
    return
   else
    individual.append(i)


