# Milestone 1

MARS_CONSTANT: float = 0.378

# Mars weight:
def mars_weight():
    user_weight: float = float(input("Write your weight? "))

    planet_weight: float = round(user_weight * MARS_CONSTANT, 2)
    return f"Your weight on mars: {planet_weight}"

my_weight_on_mars = mars_weight()
print(my_weight_on_mars)
