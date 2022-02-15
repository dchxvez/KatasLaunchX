def generate_report(first_tank, second_tank, third_tank):
    total_average = (first_tank + second_tank + third_tank) / 3
    return f"""Fuel Report:
    Total Average: {total_average}%
    First tank: {first_tank}%
    Second tank: {second_tank}%
    Thirt tank: {third_tank}% 
    """

print(generate_report(90, 50, 50)) #Reference asignation

def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

average([70, 30, 40]) 

print('updating numbers\n')

def generate_report(first_tank, second_tank, third_tank):
    return f"""Fuel Report:
    Total Average: {average([first_tank, second_tank, third_tank])}%
    First tank: {first_tank}%
    Second tank: {second_tank}%
    Thirt tank: {third_tank}% 
    """

print(generate_report(76, 20, 30))

print("-"*76)
#Second part

def mission_report(pre_launch_time, flight_time, destination, external_tank, main_tank):
    return f"""
    Mission to {destination}
    Total travel time: {pre_launch_time + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    """

print(mission_report(68, 256, "You Heart", 260510, 3006500))

print('Things to add')

def mission_report(destination, *minutes, **fuel_reservoirs):
    return f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """

print(mission_report("YOU HEART", 235, 456, main=4530250, auxiliar=3595646))

print('Final report')
def mission_report(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report

print(mission_report("You heart", 6546,56785,213, main=646786, auxiliar=649871446))