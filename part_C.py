import generatemodels
import transitionmodel
import observationmodel
import StateEstimate
import random
import numpy as np
import sys
import os

#----------------------------------------------------------------------------------------------
# SETUP
dir_path = './Ground_Truth/'

# Get the number of files requested from the user
file_name = input("Type the name of the test file you want to run (e.g. test1.txt): ")

complete_name = os.path.join(dir_path, file_name)

file_ptr = open(complete_name, 'r')

lines_ptr = file_ptr.readlines()

#----------------------------------------------------------------------------------------------
# Variables to store Read Info

#----------------------------------------------------------------------------------------------
# Read File

# Read Rows/Columns
rows = int(lines_ptr[0])
cols = int(lines_ptr[1])


# Read Initial Location
initial_location = [0,0]
initial_location[0] = int(lines_ptr[2])
initial_location[1] = int(lines_ptr[3])


# Read Actions List
actionsList = []
for i in range(100):

	actionsList.append( (lines_ptr[4 + i].split("\n"))[0] )


# Read Coordinates List
coordinatesList = []
for i in range(100):

	coordinatesList.append( (lines_ptr[104 + i].split("\n"))[0] )


# Read Observations List
observationsList = []
for i in range(100):

	observationsList.append( (lines_ptr[204 + i].split("\n"))[0] )


# Read map
myMap = []
for i in range(rows * cols):

	myMap.append( (lines_ptr[304 + i].split("\n"))[0] )


world_map = np.reshape(myMap,(rows,cols))

print("This is the World Map for the current file")
for row in world_map:
	print(row)
print()
print()
print()
#----------------------------------------------------------------------------------------------
# Apply Filtering

tm = transitionmodel.TransitionModel()
om = observationmodel.ObservationModel()
se = StateEstimate.StateEstimate()


priorprob = None #TODO: decide how to setup prior prob


# Register TM Actions
tm.registerAction("Up", generatemodels.generatetransitionmatrix("Up", world_map))
tm.registerAction("Down", generatemodels.generatetransitionmatrix("Down", world_map))
tm.registerAction("Right", generatemodels.generatetransitionmatrix("Right", world_map))
tm.registerAction("Left", generatemodels.generatetransitionmatrix("Left", world_map))

# Register OM
om.registerObservation("H",generatemodels.generateobservationalmatrix("H", world_map))
om.registerObservation("N",generatemodels.generateobservationalmatrix("N", world_map))
om.registerObservation("T",generatemodels.generateobservationalmatrix("T", world_map))


# Setup Prior Probability
total_cells = rows * cols
blocked_cells = 0

for rows in (world_map):

	for item in (rows):

		if (item == "B"):

			blocked_cells += 1

total_unblocked_cells = total_cells - blocked_cells


pp = np.zeros( world_map.shape, dtype=float)


for i in range(world_map.shape[0]):

	for j in range(world_map.shape[1]):

		if (world_map[i][j] != "B"):

			pp[i][j] = (1 / total_unblocked_cells)



# Generate Results
actions = actionsList
observations = observationsList
se.tm = tm
se.om = om
se.priorprob = pp


prob_distribution = se.executeFiltering(actions, observations, world_map.shape[0], world_map.shape[1])

#----------------------------------------------------------------------------------------------

print("Result: ")

for row in prob_distribution:
	print(row)


#----------------------------------------------------------------------------------------------

max_cell = 0
max_cell_location = [0, 0]

for i in range(world_map.shape[0]):

	for j in range(world_map.shape[1]):

		if (prob_distribution[i][j] > max_cell):

			max_cell = prob_distribution[i][j]
			max_cell_location[0] = i
			max_cell_location[1] = j

print("The Cell with the highest probability is: {}, with probability {}.".format(max_cell_location, max_cell))