# A list is like a collection of items (e.g., a shopping list).
fruits=["apple","banana","cherry"]
#accessing elements
print(fruits[0]) #output :apple
fruits[1]="orange"# modifying an element
print(fruits)#displaying all fruit with update banana by orange
#adding an element
fruits.append("grape")
print(fruits)#display all the fruits with the addtion of grape

#Tuples are like lists, but unchangeable. Once created, you can’t modify them
coorddinates=(10,20)
#accessing elements
print(coorddinates[0])# output is 10
#A set is a collection of unique items (no duplicates allowed).
unique_number={1,2,3,4,5,6}
print(unique_number)
#A dictionary is like a phonebook—it stores key-value pairs.
student_info={"name":"charile","age":80,"grade":"A"}
#accesing value by its key
print(student_info["name"])

    