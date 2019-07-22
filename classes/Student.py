from classes.Person import Person


class Student(Person):
    def display_class(self, current_class, current_stream):
        print(f"{self.name}: Class: {current_class}{current_stream}")