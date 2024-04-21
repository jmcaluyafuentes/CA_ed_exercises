# age : integer
# has_membership : boolean
# transport_type : string
def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):
    entry_ticket_cost = 15 if age < 60 else 10 # to do
    candy_cost = 5 if has_membership else 10 # to do
    parking_cost = 0 if transport_type == 'Bus' else 3 # to do

    return entry_ticket_cost + candy_cost + parking_cost

cost = calculate_total_cost_of_visiting_cinema(20, True, "Car")
print(cost)
cost = calculate_total_cost_of_visiting_cinema(65, False, "Bus")
print(cost)
cost = calculate_total_cost_of_visiting_cinema(45, False, "Car")
print(cost)
cost = calculate_total_cost_of_visiting_cinema(60, True, "Car")
print(cost)
