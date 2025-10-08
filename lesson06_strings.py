# greetings = "Hello"
# name = "Adda,"
# print(greetings + " " + name)
# message = "you have been selected for jurry duty"

# print(greetings + " " + name + " " + message)

# print(message[:6])

# long_word = "Antidisestablishmentarianism"
# print(long_word[-1:])
# print(long_word[0:28])
# print(long_word[-3::-9])
# print(long_word[:6])
# print(long_word[-8:])
# print(long_word[::2])

# country = "Uzbekistan"
# word_length = len(country) 
# print(word_length)

# phrase = "JaCkSAuL"
# print("Yo:", phrase.upper())
# print("Yo", phrase.lower())
# print("Yo", phrase.capitalize())
# print("The author:", phrase.title())

#Find and replace text 
# sentence = "I love chicken wings"
# new_sentence = sentence.replace("I","You")
# print(new_sentence)

#Formatted Strings
# name = "Frank"
# age = 2
# location = "Pittstown"
# print(f"Hello, my name is {name} I am {age} years old and live in {location}")
# print(f"Next year I'll be {age + 1}")

#Challenges
# print(len(input("Type your favorite quote:")))

# first_name = input("Type your first name:")
# last_name = input("Type your last name:")
# print(last_name + ", " + first_name)

user_word = input("Put in a word:") 
print(user_word[-1::-1].upper() + " " + user_word[-1::-1].lower() )
