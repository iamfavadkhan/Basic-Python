class Point:
    def __init__(self , a , b):
        self.a = a
        self.b = b

p = Point(3.0 , 4.0)

decimal = id(p)
hexadecimal = hex(decimal)
print("Point Object :" , p)
print("decimal :" , decimal)
print("hexadecimal :" , hexadecimal)
print("Back to decimal :",int(hexadecimal , 16))
print("is it same ?" , decimal == int(hexadecimal , 16))
methods = [method for method in dir(p) if method.startswith("__") and method.endswith("__")]
print("Methods in Point class:", methods)