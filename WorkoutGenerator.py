# You will need to change the path in lines 9, 21, and 33

import random


# Create push array

pushArray = []
pushFile = open("Path/to/push/exercises") # Input your path here

x = 0   # Start the count for the index of the array in the following loop
for currentLine in pushFile:
    pushArray.append(currentLine)
    pushArray[x] = pushArray[x].strip()
    x += 1


# Create pull array

pullArray = []
pullFile = open("Path/to/pull/exercises") # Input your path here

x = 0   # Start the count for the index of the array in the following loop
for currentLine in pullFile:
    pullArray.append(currentLine)
    pullArray[x] = pullArray[x].strip()
    x += 1


# Create leg array

legArray = []
legFile = open("Path/to/leg/exercises") # Input your path here

x = 0   # Start the count for the index of the array in the following loop
for currentLine in legFile:
    legArray.append(currentLine)
    legArray[x] = legArray[x].strip()
    x += 1


def createWorkout():

    MondayExercises = random.sample(pushArray, 8)   # Push
    MondayString = ', '.join(MondayExercises)

    TuesdayExercises = random.sample(pullArray, 8)  # Pull
    TuesdayString = ', '.join(TuesdayExercises)
   
    WednesdayExercises = random.sample(legArray, 8) # Leg
    WednesdayString = ', '.join(WednesdayExercises)
   
    ThursdayExercises = random.sample(pushArray, 8) # Push
    ThursdayString = ', '.join(ThursdayExercises)
   
    FridayExercises = random.sample(pullArray, 8)   # Push
    FridayString = ', '.join(FridayExercises)
   
    SaturdayExercises = random.sample(legArray, 8)  # Leg
    SaturdayString = ', '.join(SaturdayExercises)

    print("Monday: ", MondayString, "\n")
    print("Tuesday: ", TuesdayString, "\n")
    print("Wednesday: ", WednesdayString, "\n")
    print("Thursday: ", ThursdayString, "\n")
    print("Friday: ", FridayString, "\n")
    print("Saturday: ", SaturdayString, "\n")

createWorkout()
