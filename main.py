import os
import time

def reset():
    with open('cal.txt', 'w') as calFile:
            calFile.write('0')
    with open('protein.txt', 'w') as proteinFile:
            proteinFile.write('0')
    with open('fat.txt', 'w') as fatFile:
            fatFile.write('0')

def choosePreset():
    with open('presets.txt', 'r+') as presetFile:
        lines = presetFile.readlines()
        for line in lines:
            print(line, end ='')
        print()
        presets = dict()
        for i in range(len(lines)):
            if i == (len(lines)-1):
                presets[lines[i][0:(lines[i].index('-') - 1)]] = [lines[i][(lines[i].index('-') + 1):(lines[i].index('/')-4)], lines[i][(lines[i].index('/')+2):(lines[i].index('/',(lines[i].index('/')+1))-6)], lines[i][(lines[i].index('/',(lines[i].index('/')+1))+2):len(lines[i])-9]]
            else:
                presets[lines[i][0:(lines[i].index('-') - 1)]] = [lines[i][(lines[i].index('-') + 1):(lines[i].index('/')-4)], lines[i][(lines[i].index('/')+2):(lines[i].index('/',(lines[i].index('/')+1))-6)], lines[i][(lines[i].index('/',(lines[i].index('/')+1))+2):len(lines[i])-10]]
        u_input = input('What preset would you like to use? ')
        while u_input.lower() not in presets:
            u_input1 = input("Your input did not match the key of any preset. Would you like to make a new one or try again?('new', 'try again')")
            if u_input1.lower() == 'new':
                cal = input('Calories: ')
                fat = input('fats: ')
                protein = input('Protein: ')
                presetFile.write(f'\n{u_input} - {cal}cal / {fat}g fat / {protein}g protein')
                print(f'You selected: {u_input} which adds these macros: {cal} Calories, {fat} grams of fat, and {protein} grams of protein')
                return[cal, fat, protein]
            else:
                u_input = input('What preset would you like to use? ')
        print(f'You selected: {u_input} which adds these macros: {presets[u_input][0]} Calories, {presets[u_input][1]} grams of fat, and {presets[u_input][2]} grams of protein')
        return(presets[u_input])

def askSex():
        u_input = ''
        while not(u_input.lower() in ['m','male','f','female']):
            u_input = input("Are you Male or Female(M or F): ")
        if u_input.lower() in ['m','male']:
            return('m')
        elif u_input.lower() in ['f','female']:
            return('f')
        else:
           print('not a proper value. please try again.')

def askAge():
    u_input = ''
    while not(u_input.isnumeric()):
        u_input = input('What is your age? ')
    return int(u_input)

def askWeight():
    u_input = ''
    while not(u_input.isnumeric()):
        u_input = input('What is your weight(kilograms)? ')
    return int(u_input)

def askHeight():
    u_input = ''
    while not(u_input.isnumeric()):
        u_input = input('What is your height(centimeters)? ')
    return int(u_input)



def createNewPlan(sex, age, weight, height):
    u_input = input("Are you cutting, bulking, or maintaining?('c','b','m') ")
    while not(u_input.lower() in ['c','b','m']):
                print('ERROR: Not a valid input. Please try again')
                u_input = input("Are you cutting, bulking, or maintaining?('c','b','m') ")

    if u_input == 'c':
        adjustment = .9
    elif u_input == 'b':
        adjustment = 1.1
    elif u_input == 'm':
        adjustment = 1

    if sex == 'm':
        MC = (10 * weight) + (6.25 * int(height)) - (5 * age) + 5
    elif sex == 'f':
        MC = (10 * weight) + (6.25 * int(height)) - (5 * age) - 161

    calorieGoal = MC * adjustment
    print(f'Your calorie goal is {calorieGoal}!')
    return [u_input, MC, calorieGoal]



def run():
    if os.path.exists('info.txt'):
        t = time.localtime()
        year = t.tm_year
        month = t.tm_mon
        day = t.tm_mday
        with open('cal.txt', 'r') as calFile:
            calRead = calFile.read()
        with open('protein.txt', 'r') as proteinFile:
            proteinRead = proteinFile.read()
        with open('fat.txt', 'r') as fatFile:
            fatRead = fatFile.read()


        with open('days.txt', 'r') as dayFile:
            days = dayFile.read()
        with open('time.txt', 'r') as timeFile:
            lines = timeFile.readlines()
            lastYear = lines[0]
            lastMonth = lines[1]
            lastDay = lines[2]
            print(year)
        with open('time.txt', 'w') as timeFile:
            timeFile.writelines([str(year),'\n',str(month),'\n',str(day)])
            if os.path.exists('history.txt'):
                historyLine = ['\n',lastMonth,'/',lastDay,'/',lastYear,' ',f'Calories: {calRead} Fat: {fatRead} Protein: {proteinRead}' ]
            else:
                historyLine = [lastMonth,'/',lastDay,'/',lastYear,' ',f'Day {days} Calories: {calRead} Fat: {fatRead} Protein: {proteinRead}' ]
        with open('days.txt', 'w') as dayFile:
            if year > int(lastYear):
                days = str(int(days) +1)
                with open('history.txt', 'r+') as historyFile:
                    historyFile.writelines(historyLine)
                reset()
                dayFile.write(days)
            elif month > int(lastMonth):
                days = str(int(days) +1)
                with open('history.txt', 'r+') as historyFile:
                    historyFile.writelines(historyLine)
                reset
                dayFile.write(days)
            elif day > int(lastDay):
                days = str(int(days) +1)
                with open('history.txt', 'r+') as historyFile:
                    historyFile.writelines(historyLine)
                reset()
                dayFile.write(days)


        loop = True
        while(loop):
            with open('protein.txt', 'r') as proteinFile:
                proteinRead = proteinFile.read()
            with open('fat.txt', 'r') as fatFile:
                fatRead = fatFile.read()
            print("Enter your meal/snack/item's information. Type 'exit' to close the program after your last entry or type 'preset' to choose from your list of presets.")
            calories = input('Calories: ')
            while not(calories.isnumeric()) and calories.lower() != 'exit' and calories.lower() != 'reset' and calories.lower() != 'preset':
                print('ERROR: Not a valid input. Please try again')
                calories = input('Calories: ')
            if calories.lower() == 'exit':
                loop = False
            elif calories.lower() == 'reset':
                reset()
            else:
                if calories.lower() == 'preset':
                    foodInfo = choosePreset()
                    calories = foodInfo[0]
                    fat = foodInfo[1]
                    protein = foodInfo[2]
                else:
                    fat = input('fat: ')
                    while not(fat.isnumeric()):
                        print('ERROR: Not a valid input. Please try again')
                        fat = input('fat: ')
                    protein = input('protein: ')
                    while not(protein.isnumeric()):
                        print('ERROR: Not a valid input. Please try again')
                        protein = input('protein: ')


                with open('cal.txt', 'r') as calFile:
                    calEaten = calFile.read()
                with open('info.txt', 'r') as infoFile:
                    lines = infoFile.readlines()
                    calorieGoal = lines[0]
                    style = lines[2]

                if style =='c' or style == 'm':
                    if (calEaten + calories) > calorieGoal:
                        u_input = input('Are you sure you want to eat this. You WILL go over you calorie limit. (y or n) ')
                        while not(u_input.lower() in ['y','n']):
                            print('ERROR: Not a valid input. Please try again')
                            u_input = input('Are you sure you want to eat this. You WILL go over you calorie limit. (y or n) ')
                        if u_input.lower =='y':
                            calEaten = str(int(calEaten) + int(calories))
                            with open('cal.txt', 'w') as calFile:
                                calFile.write(calEaten)
                            print(f'Calories Eaten: {calEaten}/{calorieGoal}')
                            with open('protein.txt', 'w') as proteinFile:
                                proteinFile.write(str(int(proteinRead) + int(protein)))
                            with open('fat.txt', 'w') as fatFile:
                                fatFile.write(str(int(fatRead) + int(fat)))
                    else:
                        calEaten = str(int(calEaten) + int(calories))
                        with open('cal.txt', 'w') as calFile:
                            calFile.write(calEaten)
                        print(f'Calories Eaten: {calEaten}/{calorieGoal}')
                        with open('protein.txt', 'w') as proteinFile:
                            proteinFile.write(str(int(proteinRead) + int(protein)))
                        with open('fat.txt', 'w') as fatFile:
                            fatFile.write(str(int(fatRead) + int(fat)))
                else:
                    calEaten = str(int(calEaten) + int(calories))
                    with open('cal.txt', 'w') as calFile:
                        calFile.write(calEaten)
                    print(f'Calories Eaten: {calEaten}/{calorieGoal}')
                    with open('protein.txt', 'w') as proteinFile:
                        proteinFile.write(str(int(proteinRead) +int(protein)))
                    with open('fat.txt', 'w') as fatFile:
                        fatFile.write(str(int(fatRead) + int(fat)))
                
    else:
        with open('history.txt', 'w') as historyFile:
            pass
        with open('presets.txt', 'w') as presetFile:
            pass
        #days = 1 to set the days equal to 1 if the user does not change the value
        days = 1
        sex = askSex()
        age = askAge()
        weight = askWeight()
        height= askHeight()
        u_input = input('Are you creating a new diet or continuing a current one?("new" or "continuing") ')

        while not(u_input.lower() in ['new','coninuing']):
            print('ERROR: Not a valid input. Please try again')
            u_input = input('Are you creating a new diet or continuing a current one?("new" or "continuing") ')

        if u_input.lower() == 'new':
            plan = createNewPlan(sex, age, weight, height)
            style = plan[0]
            MC = plan[1]
            calorieGoal = plan[2]
        else:
            u_input = input('Would you like to override our automatic calorie goal?(y, n) ')
            while not(u_input.lower() in ['y','n']):
                print('ERROR: Not a valid input. Please try again')
                u_input = input('Would you like to override our automatic calorie goal?(y, n) ')

            if u_input == 'n':
                plan = createNewPlan(sex, age, weight, height)
                style = plan[0]
                MC = plan[1]
                calorieGoal = plan[2]
            else:
                #collects their calorie goal
                u_input = input('What do you want your goal to be? ')
                while type(u_input) != int:
                    print('ERROR: Not a valid input. Please try again')
                    u_input = input('What do you want your goal to be? ')
                calorieGoal = u_input

                #collects how long they have been on a diet
                u_input = input('How long have you been on this diet? ')
                while type(u_input) != int:
                    print('ERROR: Not a valid input. Please try again')
                    u_input = input('How long have you been on this diet? ')
                days = u_input
                plan = createNewPlan
                style = plan[0]
                MC = plan[1]
        with open('info.txt', 'w') as infoFile:
            infoFile.writelines([str(calorieGoal),'\n', str(MC),'\n', str(style),'\n', str(sex),'\n', str(age),'\n', str(weight),'\n', str(height)])
        with open('days.txt', 'w') as daysFile:
            daysFile.write(str(days))
        with open('time.txt', 'w') as timeFile:
            t = time.localtime()
            year = t.tm_year
            month = t.tm_mon
            day = t.tm_mday
            timeFile.writelines([str(year),'\n',str(month),'\n', str(day)])
        with open('cal.txt', 'w') as calFile:
            calFile.write(str(0))
        with open('fat.txt', 'w') as fatFile:
            fatFile.write(str(0))
        with open('protein.txt', 'w') as proteinFile:
            proteinFile.write(str(0))

run()