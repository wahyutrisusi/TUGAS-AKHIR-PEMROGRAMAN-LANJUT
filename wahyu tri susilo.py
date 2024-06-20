from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Bentuk(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Class Circle
class Circle(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Class Rectangle
class Rectangle(Bentuk):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Polymorphism
def calculate_properties(Bentuk):
    print(f"Luas: {Bentuk.area()}")
    print(f"Keliling: {Bentuk.perimeter()}")

# Membuat objek
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Abstraksi
print("Lingkaran:")
calculate_properties(circle)

print("\nPersegi Panjang:")
calculate_properties(rectangle)
