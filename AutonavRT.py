import random


# Globals
saved_stability_number = 0
saved_astro_test = 0
saved_final_duration = 0
saved_detecting_encounter_psy_score = 0
saved_actual_duration = 0


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
        print(f"Degrees of Success: {degrees_of_success}")
        return degrees_of_success
    elif y > x:
        degrees_of_failure = abs(y - x) // 10
        degrees_of_failure = -int(degrees_of_failure)
        print(f"Degrees of Failure: {degrees_of_failure}")
        return degrees_of_failure
    else:
        print("The values are equal, no degrees of success or failure.")


# Input
def base_warp():
    user_input_warp = input("Please enter your Navigation (Warp) Total: ")

    if is_positive_integer(user_input_warp):
        return int(user_input_warp)
    else:
        base_warp()

def base_psyniscience():
    user_input_psyn = input("Please enter your Psyniscience Total: ")

    if is_positive_integer(user_input_psyn):
        return int(user_input_psyn)
    else:
        base_psyniscience()

def calculate_base_duration():
    user_input_duration = input("Please enter the Routes Base Duration Total in Days: ")

    if is_positive_integer(user_input_duration):
        return int(user_input_duration)
    else:
        calculate_base_duration()


# Debug Methods
def stage0():
    global saved_final_duration
    global saved_stability_number
    base_duration = calculate_base_duration()
    roll_result, effect, durationmod, saved_stability_number = roll_route_stability()
    totalduration = base_duration * durationmod
    print(f"The Route is {effect} days")
    print("New Duration is", totalduration)
    saved_final_duration = totalduration
    return saved_final_duration

def stage1():
    psyniscience_test = roll_dice(100)
    psyniscience_base_mod = base_psyniscience()
    psyniscience_test_mod = int(input("Please enter any bonuses to Psyniscience check when Divining the Auguries, such as +10 for basic charts, +20 for detailed charts, or +20 and +30 respectively if the Navigator created these charts along with Clan Rituals if used:"))
    psyniscience_total = psyniscience_base_mod + psyniscience_test_mod
    print (f"You rolled a {psyniscience_test}")
    calculate_degrees(psyniscience_total, psyniscience_test)
    return psyniscience_base_mod

def stage2():
    omen_morale = int(input("Please put your ship's morale:"))
    omen_check = roll_dice(100)
    if omen_check > omen_morale:
        captain_command = int(input("Please put your captain's Command or Missionary Charm:"))
        captain_check = roll_dice(100)
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
    
    if roll_result <= 3:
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
    # The saved_stability_number that made Astromodification Number 20 is 1-3. 4-8 and 10 give 0 and 9 gives -20. This code block will need to be modified accordingly
    if saved_stability_number < 4:
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
    global saved_final_duration
    global saved_actual_duration
    s3_navigation_warp = int(input("Please put in the total for Navigation Warp, such as Charts, Ship Modifications and Ship Natures that could apply: "))
    navig_check = roll_dice(100)
    print (f"The roll was {navig_check}")
    modified_s3_navigation_warp = s3_navigation_warp + saved_astro_test
    degrees = calculate_degrees(modified_s3_navigation_warp,navig_check)
    if degrees <= -2:
        saved_actual_duration = saved_final_duration * 4
        return saved_actual_duration
    if degrees == -1:
        saved_actual_duration = saved_final_duration * 3
        return saved_actual_duration
    if degrees == -0:
        saved_actual_duration = saved_final_duration * 2
        return saved_actual_duration
    if degrees == 0:
        saved_actual_duration = saved_actual_duration * 1
        return saved_actual_duration
    if degrees == 1:
        saved_actual_duration = saved_final_duration * .75
        return saved_actual_duration
    if degrees == 2:
        saved_actual_duration = saved_actual_duration * .5
        return saved_actual_duration
    if degrees >= 3:
        saved_actual_duration = saved_actual_duration * .25
        return saved_actual_duration
    print(f"The Actual Duration of the Travel will be {saved_actual_duration}")



#This requires a +10 check(Which has been added now), and if they succeed by even 1 degree of success, they get a +20 to avoid the upcoming encounter. If they fail by 1, they do not get a bonus. If they fail by two or more, the encounter happens automatically.
#Want to try and make it so the user only has to put in this value once, as there are cases where the player would be better at some psy skill tests than others.
def detecting_encounters():
    global saved_detecting_encounter_psy_score
    detecting_encounters_psy_check = roll_dice(100)
    if saved_detecting_encounter_psy_score < 1:
        detecting_encounters_psy_skill = int(input("Please put in your Navigators Psyiscience Score in terms of Detecting Encounters: "))
        detecting_encounters_psy_skill = detecting_encounters_psy_skill + 10
        saved_detecting_encounter_psy_score = detecting_encounters_psy_skill
        calculate_degrees(saved_detecting_encounter_psy_score,detecting_encounters_psy_check)
        return saved_detecting_encounter_psy_score
    if saved_detecting_encounter_psy_score < detecting_encounters_psy_check:
        calculate_degrees(saved_detecting_encounter_psy_score,detecting_encounters_psy_check)
#Testing Location


#stage0()
#stage1()
#stage2()
#locate_astro()
navigation_warp()
#detecting_encounters()