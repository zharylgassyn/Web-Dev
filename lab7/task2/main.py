from models import Animal, Dog, Cat

animals = [
    Dog("Rex", 3, "brown", "German Shepherd"),
    Cat("Whiskers", 5, "white", True),
    Dog("Buddy", 2, "black", "Labrador"),
    Cat("Luna", 1, "gray", False)
]

for animal in animals:
    print(animal)
    print(f"  Info: {animal.info()}")
    print(f"  Sound: {animal.speak()}")
    
    if isinstance(animal, Dog):
        print(f"  Special: {animal.fetch()}")
    elif isinstance(animal, Cat):
        print(f"  Special: {animal.scratch()}")
    print()