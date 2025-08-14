from pathlib import Path
from fastcore.basics import patch

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


@patch
def __repr__(self: Student) -> str:
    return f"Student(name={self.name!r}, age={self.age!r})"


@patch 
def get_name(self: Student) -> str:
    return self.name


@patch
def get_age(self: Student) -> int:
    return self.age

student = Student(name="Alice", age=20)
print(student)

print(f"Name: {student.get_name()!r}")
print(f"Age: {student.get_age()!r}")