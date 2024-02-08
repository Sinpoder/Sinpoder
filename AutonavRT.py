import random


# Globals
saved_stability_number = 0
saved_astro_test = 0
saved_final_duration = 0


# Utils
def roll_dice(size):
    return random.randint(1, size)

def is_positive_integer(user_input_warp):
    try:
        number = int(user_input_warp)

        if number < 0:
            print("Invalid input. Please try again with a positive whole number.")
            return False

        return True
    except ValueError:
        return False

def calculate_degrees(x, y):
    if x > y:
        degrees_of_success = abs(x - y) // 10
        print("Degrees of Success: {degrees_of_success}")
        return degrees_of_success
    elif y > x:
        degrees_of_failure = abs(y - x) // 10
        print("Degrees of Failure: {degrees_of_failure}")
        return degrees_of_failure
    else:
        print("The values are equal, no degrees of success or failure.")


# Input
def base_warp():
    user_input_warp = input("Please enter your Navigation (Warp) Total: ")

    if is_positive_integer(user_input_warp):
        return int(user_input_warp)
    else:
        basewarp()

def base_psyniscience():
    user_input_psyn = input("Please enter your Psyniscience Total: ")

    if is_positive_integer(user_input_psyn):
        return int(user_input_psyn)
    else:
        base_psyniscience()

def base_duration():
    user_input_duration = input("Please enter the Routes Base Duration Total in Days: ")

    if is_positive_integer(user_input_duration):
        return int(user_input_duration)
    else:
        baseduration()


# Debug Methods
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
    psyniscience_test = roll_dice(100)
    psyniscience_base_mod = base_psyniscience()
    return psyniscience_base_mod
    psyniscience_test_mod = int(input("Please enter any bonuses to Psyniscience check, such as +10 for basic charts, +20 for detailed charts, or +20 and +30 respectively if the Navigator created these charts:"))
    psyniscience_total = psyniscience_base_mod + psyniscience_test_mod
    print (f"You rolled a {psyniscience_test}")
    calculate_degrees(psyniscience_total, psyniscience_test)    

def stage2():
    omen_morale = int(input("Please put your ship's morale:"))
    omen_check = roll_dice(100)
    if omen_check > omen_morale:
        captain_command = int(input("Please put your captain's Command or Missionary Charm:"))
        captain_check = roll_dice
        if captain_check > captain_command:
            print("You have successfully negated the Omen")
        else:
            print("You did not negate the Omen")
    else:
        print("Your Crew's Morale was high enough to ignore the Omen")
    print ("Determine the difficulty of the Willpower Test as the Ship Transitions into the Warp. Have your players roll for that Willpower Test, if they fail, add +10 to the Warp Travel Hallucinations chart on page 31 in the Navis Primer")


# Warp Functions
def roll_route_stability():
    print("Rolling for Route Stability")
    global saved_stability_number

    roll_result = roll_dice(10)
    saved_stability_number = roll_result
    effect = ""
    durationmod = 1
    
    if roll_result <= 4:
        effect = "Stable Route: The Navigator gains a +10 bonus on any Tests to chart this route for future use."
        durationmod = 1
    elif roll_result <= 5: # This was 6 previously, which made the next condition unreachable
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

def locate_astro():
    print("Locating the Astronomicon")

    global saved_stability_number
    global saved_astro_test

    locate_astro = base_psyniscience()
    
    if saved_stability_number < 2:
        astro_modification_number = 20
    elif saved_stability_number < 5: # Total guess on the value here, previously the next condition was unreachable
        astro_modification_number = 0
    elif saved_stability_number < 9:
        astro_modification_number = -20
    else:
        astro_modification_number = 0

    locate_astropsy = roll_dice(100)
    total_locate_astro = locate_astro + astro_modification_number

    if locate_astropsy < total_locate_astro:
        saved_astro_test = 10
        return saved_astro_test
    else:
        saved_astro_test = -20
        return saved_astro_test
        
def navigation_warp():
    global saved_astro_test
    s3_navigation_warp = int(input("Please put in the total for Navigation Warp, such as Charts, Ship Modifications and Ship Natures that could apply"))
    navig_check = roll_dice(100)

#stage0()
#stage1()
#stage2()
locate_astro()
