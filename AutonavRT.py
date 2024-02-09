import random


# Globals
saved_stability_number = 0
saved_astro_test = 0
saved_final_duration = 0
saved_detecting_encounter_psy_score = 0
saved_actual_duration = 0
saved_avoid_encounter_bonus = 0


# Utils
def roll_dice(size):
    return random.randint(1, size)

def is_positive_integer(user_input):
    try:
        number = int(user_input)

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
    print(f"The Route is {effect} ")
    print(f"New Duration is {totalduration} days")
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
    if saved_stability_number <= 3:
        astro_modification_number = 20
    elif saved_stability_number <= 4: # Total guess on the value here, previously the next condition was unreachable
        astro_modification_number = 0
    elif saved_stability_number <= 9:
        astro_modification_number = -20
    else:
        astro_modification_number = 0

    locate_astropsy = roll_dice(100)
    total_locate_astro = locate_astro + astro_modification_number

    if locate_astropsy < total_locate_astro:
        saved_astro_test = 10
        print("Navigator successfully located the Astronomican")
        return saved_astro_test
    else:
        saved_astro_test = -20
        print("Navigator wasn't able to located the Astronomican")
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
    print (degrees)
    if degrees <= -2:
        saved_actual_duration = saved_final_duration * 4
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration
    elif degrees == -1:
        saved_actual_duration = saved_final_duration * 3
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration
    elif degrees == -0:
        saved_actual_duration = saved_final_duration * 2
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration
    elif degrees == 0:
        saved_actual_duration = saved_actual_duration * 1
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration
    elif degrees == 1:
        saved_actual_duration = saved_final_duration * .75
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration
    elif degrees == 2:
        saved_actual_duration = saved_actual_duration * .5
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration
    elif degrees >= 3:
        saved_actual_duration = saved_actual_duration * .25
        print(f"The Actual Duration of the Travel will be {saved_actual_duration}")
        return saved_actual_duration


def detecting_encounters():
    global saved_detecting_encounter_psy_score
    global saved_avoid_encounter_bonus
    detecting_encounters_psy_check = roll_dice(100)
    if saved_detecting_encounter_psy_score < 1:
        detecting_encounters_psy_skill = int(input("Please put in your Navigators Psyiscience Score in terms of Detecting Encounters: "))
        detecting_encounters_psy_skill = detecting_encounters_psy_skill + 10
        saved_detecting_encounter_psy_score = detecting_encounters_psy_skill
        return saved_detecting_encounter_psy_score
    degrees = calculate_degrees(saved_detecting_encounter_psy_score,detecting_encounters_psy_check)
    if degrees >= 1:
        saved_avoid_encounter_bonus = 20
        return saved_avoid_encounter_bonus
    if degrees == -1:
        saved_avoid_encounter_bonus = 0
        return saved_avoid_encounter_bonus
    if degrees <= -2:
        saved_avoid_encounter_bonus = -100
        return saved_avoid_encounter_bonus
    

def encounter_table():
    global saved_astro_test
    encounter_table_roll = roll_dice(100)
    if encounter_table_roll <= 20:
        if saved_astro_test == -20:
            locate_astro()
        else:    
            print("All is Well. Any character suffering from Warp Travel Hallucinations can try to shake off the effects")
    elif encounter_table_roll <= 30:
        trials_of_the_soul()
        print("All Explorers and relevant NPCs must make a +0 Willpower Test or be effected by Warp Halluincation, gain +30 if Gellar fields are on")
    elif encounter_table_roll <= 40:
        trials_of_the_soul()
        print("Psychic Predators: Roll on Warp Incursions table on page 33 and apply the effect. If Gellar fields are on, reduce roll by 30")
    elif encounter_table_roll <= 50:
        avoid_encounter()
        print("Statis: The Ship has become stuck in a warp rift, add 1d5 days to journey's duration")
    elif encounter_table_roll <=60:
        trials_of_the_soul()
        print("Spontaneous Inhuman Combustion: The GM chooses one component that suddenly and inexplicably is set on fire")
    elif encounter_table_roll <= 70:
        avoid_encounter()
        print("Warp Storm: If the Gellar Field is functional, roll 1d10 twice on the critial hit table page 222 and choose the lowest. If damage, roll once and if not operational roll 1d10+2")
    elif encounter_table_roll <= 80:
        avoid_encounter()
        print("Atheric Reef: Your ship scraps against a jagged fragment of false reality. The Ship takes 1d10+2 damage, ignoring void shields. If Gellar Field is damaged, 2d10+3. If not opertional 4d10+5")
    elif encounter_table_roll <= 90:
        avoid_encounter()
        print("Warp Rift: The Vessel is thrown into a nebula of unreality for 1d10 days. Each Day they are in the nebula roll on Warp Incursions Table")
    if encounter_table_roll <= 100:
        avoid_encounter()
        print(" Your Ship is thrown back into real space, the vessel is counted as Severly Off Course.")


def trials_of_the_soul():
    trials_of_the_soul_roll = roll_dice(100)
    if trials_of_the_soul_roll <= 25:
        corruption_points = roll_dice(5)
        print(f"Trial of Temptation has occurred, if failed take {corruption_points} corruption points and the Encounter")
    elif trials_of_the_soul_roll <= 50:
        damage = roll_dice(10)
        damage = damage +2 
        print(f"A Contest of Strength has occured, if failed take {damage} Damage, ignoring armor and toughness and the Encounter")
    elif trials_of_the_soul_roll <= 75:
        insanity_points = roll_dice(5)
        print(f"A Trial of Endurance has occured, if failed take {insanity_points} insanty points and the Encounter")
    elif trials_of_the_soul <= 100:
        insanity_points = roll_dice(5)
        print(f"A Conundrum has occured, if failed, loses one unspent fate point and can not regain it until they re-enter real space. If no Fate Points are avaliable take {insanity_points} insanity Points and the Encounter")

def avoid_encounter():
    global saved_avoid_encounter_bonus
    if saved_avoid_encounter_bonus <= -100:
        print("Navigator was unable to see this encounter coming and the Encounter Automatically Triggers")
    else:
        avoiding_physical_encounter_roll = roll_dice(100)
        avoiding_encounters_warp_skill = int(input("Please put in your Navigators Base Warp Navigation Skill(No External Bonuses): "))
        avoiding_encounters_warp_skill = avoiding_encounters_warp_skill + saved_avoid_encounter_bonus
        if avoiding_physical_encounter_roll <= avoiding_encounters_warp_skill:
            print("Your Navigator has warned your helmsman to move the ship to avoid an encounter")
            avoiding_physical_encounter_pilot_roll = roll_dice(100)
            avoiding_physical_encounters_pilot_skill = int(input("Please put in your helmsman's Pilot (Space Craft) skill: "))
            avoiding_physical_encounters_pilot_skill = avoiding_physical_encounters_pilot_skill +10
            if avoiding_physical_encounter_pilot_roll > avoiding_physical_encounter_pilot_roll:
                print("Your helmsman has managed to avoid the encounter")
            else:
                print("Your helmsman is not able to avoid the encounter! Please see description of encounter")
        else:
            print("Your Navigator has missed this physical encounter and has ran directly into it! Please see description of encounter")



def travelling_thr_warp():
    global saved_actual_duration
    travel_actual_duration = saved_actual_duration / 5
    if travel_actual_duration < 1:
        travel_actual_duration = 1
    counter = 0
    while counter < travel_actual_duration:
        encounter_table()
        counter += 1

#Testing Location


stage0()
stage1()
stage2()
locate_astro()
navigation_warp()
detecting_encounters()
travelling_thr_warp()
