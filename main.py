import math

class Circle:
    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def compute_area(self):
        """Compute the area of the circle."""
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        """Compute the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Example usage
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.compute_area():.2f}")
print(f"Perimeter of the circle: {circle.compute_perimeter():.2f}")
