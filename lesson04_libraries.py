#Python libraries are repositories of code that can be imported into your own repo

#Math library
import math
print("\n--- Math Library ---\n")
print("Square root:", math.sqrt(25))
print("Round up:", math.ceil(4.1))
print("Round down:", math.floor(4.5) )
print("Power:", math.pow(2,5))
print("Pi:", math.pi)

#Random Library
#Psuedorandom number generator- Can be random enough. Pick a random number like the date, this is a Seed then divide it by another randomw number and then subtract and add and so on
#But to be truly random you must use something from real life that is truly random i.e. the temperature a video or a phohto
#True random number generator- Can only be achived in real life

seed = 182.74
seedpt2 = math.sqrt(seed)
seedpt3 = math.pow(seedpt2,5)
print(seedpt3)
