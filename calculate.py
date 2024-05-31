import triangle
import rectangle

def calculate_shape_properties(shape, *dimensions):
    if shape == "triangle":
        if len(dimensions) != 3:
            raise ValueError("Triangle requires 3 dimensions: base, height, and third side.")
        base, height, third_side = dimensions
        area = triangle.area(base, height)
        perimeter = triangle.perimeter(base, height, third_side)
    elif shape == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires 2 dimensions: length and width.")
        length, width = dimensions
        area = rectangle.area(length, width)
        perimeter = rectangle.perimeter(length, width)
    else:
        raise ValueError("Unsupported shape. Supported shapes: triangle, rectangle.")
    
    return area, perimeter

	
if __name__ == "__main__":
    shape = input("Enter the shape (triangle/rectangle): ").strip().lower()
    if shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        third_side = float(input("Enter the third side of the triangle: "))
        area, perimeter = calculate_shape_properties(shape, base, height, third_side)
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area, perimeter = calculate_shape_properties(shape, length, width)
    else:
        print("Unsupported shape.")
        exit(1)
    
    print(f"The area of the {shape} is: {area}")
    print(f"The perimeter of the {shape} is: {perimeter}")