from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# print("Hello World")
# x = 5
# print(x)
# weapons = ['sword', 'gun', 'knife']
# print(weapons)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Sam = Person('Sam', 21)

# print(Sam.name, Sam.age)

# def addNumbers(num1, num2):
#     print(num1 + num2)

# addNumbers(1, 2)
# addNumbers(5, 5)