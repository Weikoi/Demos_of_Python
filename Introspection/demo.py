

class Student(object):
    def __init__(self, age=18, name="unknown"):
        self.age = age
        self.name = name

    def introduce(self):
        print("My name is" + self.name)


if __name__ == '__main__':
    """
    自省的常用函数:
    """
    print(dir(Student))
    print(type(Student))

    a = Student(20, "Jim")
    print(getattr(a, "name"))
    print(hasattr(a, "age"))
    setattr(a, "School name", "Fudan High School")
    print(getattr(a, "name"))
    print(isinstance(a, Student))