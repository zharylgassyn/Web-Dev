class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def speak(self):
        return "Some sound"
    
    def info(self):
        return f"{self.name} is {self.age} years old and {self.color}"
    
    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
    
    def speak(self):
        return "Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"
    
    def __str__(self):
        return f"Dog: {self.name} ({self.breed})"

class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age, color)
        self.indoor = indoor
    
    def speak(self):
        return "Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture"
    
    def __str__(self):
        indoor_status = "indoor" if self.indoor else "outdoor"
        return f"Cat: {self.name} ({indoor_status})"