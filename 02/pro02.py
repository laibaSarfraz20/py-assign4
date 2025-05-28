def main():
    mass = float(input("Enter mass in kilograms: "))
    c = 3e8  # speed of light in m/s
    energy = mass * c ** 2
    print("The energy is", energy, "joules")

if __name__ == '__main__':
    main()
