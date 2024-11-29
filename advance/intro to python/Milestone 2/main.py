# Milestone 2:

MERCURY_CONSTANT: float = 0.376
VENUS_CONSTANT: float = 0.889
MARS_CONSTANT: float = 0.378
JUPITER_CONSTANT: float = 2.360
SATURN_CONSTANT: float = 1.081
URANUS_CONSTANT: float = 0.815
NEPTUNE_CONSTANT: float = 1.140

def calculate_weight():
    while True:
        try:
            user_weight = float(input("Enter your weight on Earth: "))
            break
        except ValueError:
            print("It must be Numeric value")
    
    
    planet_name = input("Enter the planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, or Neptune): ")

    if planet_name.lower() == "mercury":
        weight = user_weight * MERCURY_CONSTANT
    elif planet_name.lower() == "venus":
        weight = user_weight * VENUS_CONSTANT
    elif planet_name.lower() == "mars":
        weight = user_weight * MARS_CONSTANT
    elif planet_name.lower() == "jupiter":
        weight = user_weight * JUPITER_CONSTANT
    elif planet_name.lower() == "saturn":
        weight = user_weight * SATURN_CONSTANT
    elif planet_name.lower() == "uranus":
        weight = user_weight * URANUS_CONSTANT
    elif planet_name.lower() == "neptune":
        weight = user_weight * NEPTUNE_CONSTANT
    else:
        print("Invalid planet name.")
        return

    print(f"Your weight on {planet_name} is {weight:.2f}")

calculate_weight()

    
# 2ND WAY TO RESSOLVE:

gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 1.140
}

def calculate_weight_on_planet(earth_weight, planet):
    if planet in gravity_constants:
        weight_on_planet = earth_weight * gravity_constants[planet]
        return f"Your weight on {planet} is: {weight_on_planet:.2f}"
    else:
        return None  # Explicitly return None for invalid planet names

def main():
    # Validate earth weight input
    while True:
        try:
            earth_weight = float(input("Enter your weight on Earth: "))
            break
        except ValueError:
            print("It must be a numeric value. Please try again.")

    # Validate planet input
    while True:
        planet = input("Enter the name of the planet in our solar system: ").title()  # Capitalize the first letter
        result = calculate_weight_on_planet(earth_weight, planet)
        if result:
            print(result)
            break  # Exit the loop if valid
        else:
            print("Invalid planet name. Please try again.")

main()
