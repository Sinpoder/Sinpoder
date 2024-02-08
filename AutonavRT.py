# -*- coding: utf-8 -*-

import random
def diceroll1d100():
    d100diceroll= random.randint(1,100)
    return d100diceroll
diceroll1d10 = random.randint(1,10)
diceroll1d5 = random.randint(1,5)
saved_stability_number = 0
saved_astro_test = 0
saved_final_duration = 0


def validate_input(user_input_warp):
    try:
        # Convert input to an integer
        number = int(user_input_warp)
        # Check if the number is positive
        if number < 0:
            return False
        return True
    except ValueError:
        return False


def validate_input_psyn(user_input_psyn):
    try:
        # Convert input to an integer
        number = int(user_input_psyn)
        # Check if the number is positive
        if number < 0:
            return False
        return True
    except ValueError:
        return False

def validate_input_duration(user_input_duration):
    try:
        # Convert input to an integer
        number = int(user_input_duration)
        # Check if the number is positive
        if number < 0:
            return False
        return True
    except ValueError:
        return False


def basewarp():
    user_input_warp = input("Please enter your Navigation (Warp) Total: ")
    if validate_input(user_input_warp):
        print("Navigation (Warp):", user_input_warp)
        return int(user_input_warp)
    else:
        print("Error: Invalid input. Please try again.")
        basewarp()

def basepsyn():
    user_input_psyn = input("Please enter your Psyniscience Total: ")
    if validate_input_psyn(user_input_psyn):
        print("Total Psyniscience:", user_input_psyn)
        return int(user_input_psyn)
    else:
        print ("Error: Invalid Input. Please try again with a positive whole number.")
        basepsyn()

def baseduration():
    user_input_duration = input("Please enter the Routes Base Duration Total in Days: ")
    if validate_input_duration(user_input_duration):
        print("Total Base Duration:", user_input_duration)
        return int(user_input_duration)
    else:
        print ("Error: Invalid Input. Please try again with a positive whole number.")
        baseduration()
        
def stage0():
    global saved_final_duration
    base_duration = baseduration()
    roll_result, effect, durationmod = roll_route_stability()
    totalduration = base_duration * durationmod
    print(f"The Route is {effect} days")
    print("New Duration is", totalduration)
    saved_final_duration = totalduration
    return saved_final_duration


def stage1():
    psyniscience_test = diceroll1d100()
    psyniscience_base_mod = basepsyn()
    return psyniscience_base_mod
    psyniscience_test_mod = int(input("Please enter any bonuses to Psyniscience check, such as +10 for basic charts, +20 for detailed charts, or +20 and +30 respectively if the Navigator created these charts:"))
    psyniscience_total = psyniscience_base_mod + psyniscience_test_mod
    print (f"You rolled a {psyniscience_test}")
    calculate_degrees(psyniscience_total,psyniscience_test)    

def calculate_degrees(x, y):
    if x > y:
        degrees_of_success = abs(x - y) // 10
        print(f"Degrees of Success: {degrees_of_success}")
        return degrees_of_success
    elif y > x:
        degrees_of_failure = abs(y - x) // 10
        print(f"Degrees of Failure: {degrees_of_failure}")
        return degrees_of_failure
    else:
        print("The values are equal, no degrees of success or failure.")

def roll_route_stability():
    global saved_stability_number
    roll_result = random.randint(1, 10)
    saved_stability_number = roll_result
    effect = ""
    durationmod = 1
    if roll_result in range(1, 4):
        effect = "Stable Route: The Navigator gains a +10 bonus on any Tests to chart this route for future use."
        durationmod = 1
    elif roll_result in range(4, 6):
        effect = "Indirect Path: Double the GMs Calculation of Duration"
        durationmod = 2
    elif roll_result == 6:
        effect = "Haunted Passage: Double the GMs Calculation of Duration and add +10 to any rolls made on Table 25: Warp Travel Hallucinations."
        durationmod = 2
    elif roll_result == 7:
        effect = "Surly Route: Double the GMs Calculation of Duration and the Navigator suffers a 10 penalty on his Psyniscience Test in Divining the Auguries."
        durationmod = 2
    elif roll_result == 8:
        effect = "Untraceable Trail: Double the GMs Calculation of Duration and the route cannot be charted."
        durationmod = 2
    elif roll_result == 9:
        effect = "Lightless Path: Double the GMs Calculation of Duration and the Astronomican is obscured for the trip."
        durationmod = 2
    elif roll_result == 10:
        effect = "Byzantine Route: Triple the GMs Calculation of Duration."
        durationmod = 3

    return roll_result, effect, durationmod, saved_stability_number


def stage2():
    omenmorale = int(input("Please put your ship's morale:"))
    omencheck = diceroll1d100()
    if omencheck > omenmorale:
        captaincommand = int(input("Please put your captain's Command or Missionary Charm:"))
        captaincheck = diceroll1d100
        if captaincheck > captaincommand:
            print("You have successfully negated the Omen")
        else:
            print("You did not negate the Omen")
    else:
        print("Your Crew's Morale was high enough to ignore the Omen")
    print ("Determine the difficulty of the Willpower Test as the Ship Transitions into the Warp. Have your players roll for that Willpower Test, if they fail, add +10 to the Warp Travel Hallucinations chart on page 31 in the Navis Primer")
            
    


def locateastro():
    global saved_stability_number
    global saved_astro_test
    print("Locating the Astronomicon")
    locateastro = basepsyn()
    astrostabilitynumber = saved_stability_number
    if astrostabilitynumber < 2:
        astromodificationnumber = 20
    elif 2 < astrostabilitynumber < 9:
        astromodificationnumber = 0
    elif 9 < astrostabilitynumber < 9:
        astromodificationnumber = -20
    elif 10 >= astrostabilitynumber:
        astromodificationnumber = 0
    locateastropsy = diceroll1d100()
    totallocateastro = locateastro + astromodificationnumber
    if locateastropsy < totallocateastro:
        saved_astro_test = 10
        return saved_astro_test
    else:
        saved_astro_test = -20
        return saved_astro_test
        


def navigwarp():
    global saved_astro_test
    s3navigationwarp = int(input("Please put in the total for Navigation Warp, such as Charts, Ship Modifications and Ship Natures that could apply"))
    navigcheck = diceroll1d100()
    
    


#stage0()
#stage1()
#stage2()
locateastro()
