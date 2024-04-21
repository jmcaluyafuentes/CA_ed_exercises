def calculate_rocket_fuel_required(distance):
   fuel_minimum = 100
   fuel_based_on_distance = distance * 15
   if (fuel_based_on_distance < fuel_minimum):
      fuel_required = fuel_minimum
   else:
      fuel_required = fuel_based_on_distance
   return(fuel_required)

fuel_required = calculate_rocket_fuel_required(10)
print(fuel_required)
fuel_required = calculate_rocket_fuel_required(1)
print(fuel_required)
fuel_required = calculate_rocket_fuel_required(20)
print(fuel_required)
