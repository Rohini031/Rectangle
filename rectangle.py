import sys

length = float(sys.argv[1])
breadth = float(sys.argv[2])

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of Rectangle =", area)
print("Perimeter of Rectangle =", perimeter)