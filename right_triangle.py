# right triangle
def input_data():
    while True:
        try:
            num = int(input())
            if num >= 2:
                return num
                break
            else:
                print("Input an integer greater than 2 please")
                print()
        except ValueError:
            print("Input value shall be an integer, not a float, or string")
            print()

def draw_triangle(side):
    for i in range(1, side+1):
        print("*" * i)
    print()
    for i in range(side,0,-1):
        print("*" * i)
    print()
    for i in range(1, side+1):
        print(" " * (side-i), end = "")
        print("*" * i)
    print()
    for i in range(side,0,-1):
        print(" " * (side-i),end = "")
        print("*" * i)

if __name__ == '__main__':
    print("Enter the length of a side of the triangle: ")
    side = input_data()

    draw_triangle(side)