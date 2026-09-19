"""
Project structure
    keep data seperate
    use clear names
    simple structure
    test as you go
"""

"""
Python paths

#os.getcwd() returns the working directory

Files
open() - file reading functions
use forward slashes data/sales_analyser.py

    with open("data/sales.csv", "r") as file:
        content = file.read()

Modules
Use import statements
    import mymodule
    from folder.utils import helper
"""

"""
Error handling:
    Syntax error
    Runtime error
        zerodivisionerror
        nameerror
        TypeError
        ValueError
        IndexError
        AttributeError

Try block contains the code that might fail and except block runs if an error happens
Code in finally always runs, error or not
"""
try:
    with open("data.txt","r") as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find file")
else:
    print(f"File is found{len(content)} characters")
print("Done")

#Re raising critical errors
try:
    func()
except Exception as e:
    print(f"Critical error: {e}")
    raise

"""
Classes
Object Oriented Programming
    way to organize code by grouping related data and functions together

    Class is a blueprint for creating objects. It defines:
        Attributes: What data the object store
        Methods: What the object can do

Working with classes follows a simple pattern:
    Define the class - Create a blueprint with the class keyword
    Add an __init__ method - Set up initial data when objects are created
    Create instances - Make actual objects from your class
    Access the data - Use the attributes you defined

    self - refers to current object. It how an object keeps track of its own data

    Instances: What we create from the class

Methods and attributes
    Attributes: storing data
        Instance attribute: unique to each object
        Class attribute: Shared by all people

Inheritance
Lets you create new classes based on exisiting ones. The new class (child)
gets everything from parent class, plus can add its own stuff

Override - Child classes can change how parents methods work (methods with same name)
"""
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

#instances
dev_config = APIConfig("api_key",max_tokens=500)
prod_config = APIConfig(api_key="api_key", model="gpt-4", max_tokens=1000)

print(dev_config.model)
print(prod_config.max_tokens)


"""
Example 2
"""
class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid format {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 100:
            self.errors.append(f"Invalid age {age}")
            return False
        return True

    def get_errors(self):
        return self.errors

validator = DataValidator() #Object

validator.validate_email(email="roshan-gmail.com") #Instance
validator.validate_age(age=150)

print(validator.get_errors())

"""
AI examples
"""

class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = True

    def load(self):
        print(f"Loading {self.model_name}")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()

        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed text {text}"

model = TextModel(model_name="gpt-4", max_length=1000)

result = model.process_text(text="Hello world")
print(result)