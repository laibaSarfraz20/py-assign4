def main():
    degrees_fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius: float = (degrees_fahrenheit - 32) * 5.0 / 9.0
    print("Temperature:", str(degrees_fahrenheit) + "F =", str(degrees_celsius) + "C")

if __name__ == '__main__':
    main()
