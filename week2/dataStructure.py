# Task 1: Create a list of integers and compute the sum
int_list = input("Enter a list of integers separated by spaces: ")
int_list = [int(num) for num in int_list.split()]
total = sum(int_list)
print(f"Sum of the integers: {total}")

print("\n" + "-"*40 + "\n")

# Task 2: Tuple of book names and print each on a new line
books = ("1984", "To Kill a Mockingbird", "The Hobbit", "Pride and Prejudice", "The Alchemist")
print("Favorite Books:")
for book in books:
    print(book)

print("\n" + "-"*40 + "\n")

# Task 3: Dictionary to store person info from user input
person = {}
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")
print("Person Information:", person)

print("\n" + "-"*40 + "\n")

# Task 4: Create two sets and find their intersection
set1 = set(map(int, input("Enter integers for Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (space-separated): ").split()))
common_elements = set1 & set2
print(f"Common elements: {common_elements}")

print("\n" + "-"*40 + "\n")

# Task 5: List comprehension for odd-length words
words = ["apple", "banana", "kiwi", "mango", "pineapple", "fig"]
odd_length_words = [word for word in words if len(word) % 2 == 1]
print("Words with odd number of characters:", odd_length_words)
