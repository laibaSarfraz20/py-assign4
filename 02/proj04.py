import math

def main():
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = math.sqrt(a**2 + b**2)
    print("The hypotenuse is", c)

if __name__ == '__main__':
    main()
