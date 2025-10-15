animals = ["donkey", "chicken", "penguin"]
numbers = [1, 3, 8, 9]
random = [1, "hi", True, 9.99]
print("First element;",  animals[0])
print("Second element;", animals[1])
print("The last element;", animals[-1])
animals[0] = "Baboon" 
animals.append("Dog")
animals.insert("Penguin", "Monkey")
animals.remove("chicken")
print(animals)
last_animal = animals.pop
