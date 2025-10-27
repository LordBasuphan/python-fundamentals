# # animals = ["Cow", "Sheep", "Donkey", "Cat", "Dog",]
# # import time 
# # for x in animals:
# #     print("Now petting:", x)
# #     time.sleep(2)
# # print("Now I am done")

# for i in range(2,10):
#     print("Counting", i)

# for_word = "Shennanigan"
# letter_list = []
# for letter in for_word:
#     letter_list.append(letter)
# print(letter_list)

#while loops

# count = 0 
# while count < 5:
#     print(f"Loopin, We are on loop number {count}")
#     count += 1
# print("loop is done")

# user_input = ""
# while user_input != "exit":
#     user_input = input("Try to escape:")

count = 60
increment = 1

while count > 1:
    increment += 1
    count -= increment

     if count < 0:
        break

    print(count)