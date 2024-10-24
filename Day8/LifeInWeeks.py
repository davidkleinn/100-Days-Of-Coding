

def life_in_weeks(age):
    age *= 52

    goal = 90 * 52
    
    weeksLeft = goal - age
    
    print(f"You have {weeksLeft} weeks left.")


life_in_weeks(56)