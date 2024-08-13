import pandas as pd

#helper - delay cost calculator 
def delay_cost_calculator(delay_time, free_time, delay_cost_per_min):
    if pd.isna(delay_time) or delay_time <= free_time:
        return 0
    else:
        return (delay_time - free_time) * delay_cost_per_min

#helper - airport cost calculator
def airport_cost_calculator(type_of_airport):
    if type_of_airport == 'large_airport':
        return 10000
    elif type_of_airport =='medium_airport':
        return 5000
    else:
        return None

def total_cost_calculator(departure_delay_time, arrival_delay_time, distance, airport_type_origin, airport_type_destination, fuel_and_other_cost):
    
    #part 1 - delay cost = departure delay + arrival delay
    departure_delay_cost = delay_cost_calculator(departure_delay_time, 15, 75)
    arrival_delay_cost = delay_cost_calculator(arrival_delay_time, 15, 75)
    delay_cost = departure_delay_cost + arrival_delay_cost

    #part 2 - airport cost
    if airport_type_origin == 'medium_airport' or airport_type_origin == 'large_airport':
        airport_cost_origin = airport_cost_calculator(airport_type_origin)
    else:
        return None

    if airport_type_destination == 'medium_airport' or airport_type_destination == 'large_airport':
        airport_cost_destination = airport_cost_calculator(airport_type_destination)
    else:
        return None

    #part 3 - fuel cost maintaince
    if isinstance(distance, (float, int)):
        fuel_maintenance_cost = float(abs(distance))* (fuel_and_other_cost)
    else:
        return None
        
    return (delay_cost + fuel_maintenance_cost + airport_cost_origin + airport_cost_destination)
    