# Constant: Speed of light in m/s
C = 299792458  # meters per second

def calculate_energy():
    """
    Ask the user for mass input, calculate energy using Einstein's formula, 
    and display the result.
    """
    try:
        # Get mass input from the user
        mass = float(input("Enter mass in kilograms: "))
        
        # Calculate energy
        energy = mass * C**2
        
        # Display results
        print("\nCalculating energy using E = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!")
    except ValueError:
        print("Invalid input! Please enter a numeric value for mass.")

def main():
    """
    Main function to drive the program.
    """
    print("Welcome to Einstein's Mass-Energy Calculator!")
    calculate_energy()

# Run the program
if __name__ == "__main__":
    main()
