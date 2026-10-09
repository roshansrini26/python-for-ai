print("Artificial Intelligence")

#python errors
#syntaxerror print("Hello World)
#name error is_true = TRUE | is_true = true
#Indexerror Out of range
#Keyerror Key not found in dictionary


"""
Basics of Python
1. variables > Comments
2. Data types > Numbers > Strings > Booleans
3. Operators
    Calculate: +, -, *, /, // (gives integer value), % (modulus), ** (exponent)
    Compare: >, <, ==
    Combine: and, or, not
        AND - both must be true
        OR - at least one must be true
        NOT - reverses the value
4. String manipulation
    Using + to join
    Using f-strings to format
    Changing cases:
        text = "Python Programming"

        print(text.lower())      # "python programming"
        print(text.upper())      # "PYTHON PROGRAMMING"
        print(text.title())      # "Python Programming"

    Cleaning strips:
        strip() - removes whitespace from the beginning and end of a string
        price = "$19"
        print(price.strip("$"))  # "19"

    Find and replace:

    message = "I love Python programming with Python"

    # Check if something exists
    print("Python" in message)        # True
    print(message.startswith("I"))   # True
    print(message.endswith("Python")) # True

    # Find position
    print(message.find("Python"))     # 7 (first occurrence)
    print(message.count("Python"))    # 2 (number of times)

    # Replace
    new_message = message.replace("Python", "JavaScript")
    print(new_message)  # "I love JavaScript programming with JavaScript"

"""

"""
Control Flow:
    if then

    age = 18
    if age >= 18:
        print("You are an adult.")

    if else
    age = 18
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

    if elif else

    nested if statements
    has_ticket = True
    age = 15

    if has_ticket:
        if age >= 18:
            print("Enjoy the movie!")
        else:
            print("Need adult supervision")
    else:
        print("Buy a ticket first")

Loop:

For loops
    for i in range(5):
        print(i)  # prints 0, 1, 2, 3, 4. #zero-indexing

    range(start, stop, step)

    Loop through text
    text = "Python"
    for char in text:
        print(char)

    Loop through a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"I love {fruit}")

While loops
A while loop continues to execute as long as a condition is true.

    count = 0
    while count <5:
        print(count)
        count += 1        
"""

"""
Data Structures:

Think of data structures as containers:
Lists: Like a shopping list (ordered items)
Dictionaries: Like a phone book (name > number)
Tuples: Like coordinates (fixed values)
Sets: Like a bag of unique items

Which one to use?

Lists: When order matters and you need to change items
Dictionaries: When you need to look up values by name
Tuples: When data shouldn’t change (like coordinates)
Sets: When you only care about unique values


Lists:
A list is a collection of items that are ordered and changeable. Lists are written with square brackets.
    fruits = ["apple", "banana", "cherry"] #can mix different data types

    accessing list items
        print(fruits[0])  # "apple"
        print(fruits[-1]) # "cherry" (last item)
    slicing lists
        print(fruits[1:3])  # ["banana", "cherry"]
        print(fruits[:2])   # ["apple", "banana"]
        print(fruits[2:])   # ["cherry"]
    changing list items
        fruits[1] = "blueberry"
    Adding items to a list
        fruits.append("orange")  # adds to the end
        fruits.insert(1, "kiwi")  # adds at index 1
    Removing items from a list
        fruits.remove("banana")  # removes first occurrence
        fruits.pop()  # removes last item
        del fruits[0]  # removes item at index 0

    List methods:
        fruits.sort()  # sorts the list in ascending order
        fruits.reverse()  # reverses the list
        print(len(fruits))  # prints the number of items in the list
        count = fruits.count("apple")  # counts occurrences of "apple"
        index = fruits.index("cherry")  # finds the index of "cherry"

Dictionaries:
A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed.

    student = {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    }
    also student = dict(name="Alice", age=20, grade="A")

    accessing dictionary values
        print(student["name"])  # "Alice"
        print(student.get("age"))  # 20

    changing dictionary values
        student["age"] = 21

    Adding items to a dictionary
        student["major"] = "Computer Science"

    Removing items from a dictionary
        student.pop("grade")  # removes the "grade" key-value pair
        del student["age"]  # removes the "age" key-value pair

    Dictionary methods
        print(student.keys())  # prints all keys
        print(student.values())  # prints all values
        print(student.items())  # prints all key-value pairs
        print(student.update({"age": 22}))  # updates the "age" key-value pair

    Nested dictionaries
        students = {
            "student1": {"name": "Alice", "age": 20},
            "student2": {"name": "Bob", "age": 22}
        }

Tuples:
A tuple is a collection of items that are ordered and unchangeable. Tuples are written with round brackets.
    coordinates = (10, 20)
    A single item tuple must have a comma after the item, like this: single_item_tuple = (10,)

    Accessing tuple items
        print(coordinates[0])  # 10
    Tuples are immutable, so you cannot change their items after creation.
    Slicing tuples works the same way as lists.

    Tuple Unpacking
        x, y = coordinates  
        a,b,c = 1,2,3 #Multiple assignment
        x,y = y,x #Swapping values

Sets:
A set is a collection of unique items that are unordered and unindexed. Sets are written with curly brackets.
    fruits = {"apple", "banana", "cherry"}
    fruits = set(["apple", "banana", "cherry"]) #using set() constructor
    removes duplicates automatically
    Use set() for empty set, {} creates an empty dictionary.

    adding items to a set
        fruits.add("orange")
    removing items from a set
        fruits.remove("banana")  # raises KeyError if not found
        fruits.discard("banana")  # removes item if found, but doesn't raise an error if not found

    Remove duplicates from a list using set
        numbers = [1, 2, 2, 3, 4, 4, 5]
        unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]

    Fast membership testing
        if "apple" in fruits:
            print("Apple is in the set")
"""