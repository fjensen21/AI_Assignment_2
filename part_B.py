import generatemodels
import transitionmodel
import observationmodel
import StateEstimate
import random
import numpy as np
import sys
import os

#----------------------------------------------------------------------------------------------

dir_path = './Test_Cases/'


# Get the number of files requested from the user
num_files = int(input("Please provide the number of files to be generated: "))


#----------------------------------------------------------------------------------------------
# Generate that many test files
for file in range(num_files):

    current_name = "test{}.txt".format( (file + 1) )

    complete_name = os.path.join(dir_path, current_name)

    #-----------------------------------------------------
    # Now write on each file the corresponding data
    file_ptr = open(complete_name, 'w')


    #-----------------------------------------------------
    # Program Logic
    rows = random.randint(1, 100)
    cols = random.randint(1, 50)

    file_ptr.write("Rows: {}\n".format(rows))
    file_ptr.write("Columns: {}\n".format(cols))

    file_ptr.write("----------------------------------------\n")


    #-----------------------------------------------------
    # Creates a random board with weighted probabilities
    location = [0,0]

    states = ["N","H","T","B"]
    startmap = random.choices(states, weights=(50, 20, 20, 10), k=(rows*cols))
    myMap = np.array(startmap)
    map = np.reshape(myMap,(rows,cols))


    observations = []

    # Initial Position (x, y)

    location[0] = random.randint(0, (rows - 1))
    location[1] = random.randint(0, (cols - 1))

    while(map[location[0]][location[1]]=="B"): #makes sure not a border

        location[0] = random.randint(0, (rows - 1))
        location[1] = random.randint(0, (cols - 1))


    file_ptr.write("X_initial: {}\n".format(location[0]))
    file_ptr.write("Y_initial: {}\n".format(location[1]))

    file_ptr.write("----------------------------------------\n")


    # #create random list of directions
    directions = ["Up","Down","Left","Right"]
    directionList = random.choices(directions, weights=(25,25,25,25), k=100)

    file_ptr.write("Actions List\n")
    for item in (directionList):
        file_ptr.write("{}\n".format(item))

    file_ptr.write("----------------------------------------\n")


    #find traveled directins 90% chance of successful travel
    file_ptr.write("Coordinates\n")

    for item in directionList:

        roll = random.randint(0, 99)

        if roll >=10:

            if item == "Up":
                if location[0] == 0 or map[location[0] - 1][location[1]] == "B": # Cell is on top row
                    location[0] = location[0]
                else:
                    location[0] = location[0] - 1

            elif item == "Down":
                if location[0] == (rows - 1) or map[location[0] + 1][location[1]] == "B":  # Cell is on bottom row
                    location[0] = location[0]
                else:
                    location[0] = location[0] + 1

            elif item == "Left":
                if location[1] == 0 or map[location[0]][location[1] - 1] == "B":  # Cell is on leftmost col
                    location[1] = location[1]
                else:
                    location[1] = location[1] - 1

            else:
                if location[1] == (cols - 1) or map[location[0]][location[1] + 1] == "B":  # Cell is on rightmost col
                    location[1] = location[1]
                else:
                    location[1] = location[1] + 1


        # Failed to move
        else:

            location[0] = location[0]
            location[1] = location[1]

        file_ptr.write("({}, {})\n".format(location[0], location[1]))

        #finds the observations atht    
        roll = random.randint(0, 99)

        if roll >=10:

            observations.append(map[location[0]][location[1]])

        else:

            roll = random.randint(0, 99)

            if (map[location[0]][location[1]] == "N"):

                if roll < 50:
                    observations.append("H")

                else:
                    observations.append("T")


            elif (map[location[0]][location[1]] == "H"):

                if roll < 50:
                    observations.append("N")

                else:
                    observations.append("T")


            elif (map[location[0]][location[1]] == "T"):

                if roll < 50:
                    observations.append("N")

                else:
                    observations.append("H")

    file_ptr.write("----------------------------------------\n")
    file_ptr.write("Observations\n")

    for item in (observations):

        file_ptr.write("{}\n".format(item))