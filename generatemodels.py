
# Given a direction and dimensions generates the transition matrix for the direction
# Directions can be "Up", "Down", "Right", "Left"
def generatetransitionmatrix(direction:str, map:list[list])->list[list]:
    # Generate empty mat with 0s
    rows = len(map)
    cols = len(map[0])

    mat = []
    for i in range(rows):
        row = [0 for j in range(cols)]
        mat.append(row)

    for i in range(rows):
        for j in range(cols):
            # Apply transition model to cell
            if direction == "Up":
                if i == 0 or map[i - 1][j] == "B": # Cell is on top row
                    mat[i][j] += 1
                else:
                    mat[i - 1][j] += .9
                    mat[i][j] += .1
            elif direction == "Down":
                if i == rows - 1 or map[i + 1][j] == "B":  # Cell is on bottom row
                    mat[i][j] += 1
                else:
                    mat[i + 1][j] += .9
                    mat[i][j] += .1
            elif direction == "Left":
                if j == 0 or map[i][j - 1] == "B":  # Cell is on leftmost col
                    mat[i][j] += 1
                else:
                    mat[i][j - 1] += .9
                    mat[i][j] += .1
            else:
                if j == cols - 1 or map[i][j + 1] == "B":  # Cell is on rightmost col
                    mat[i][j] += 1
                else:
                    mat[i][j + 1] += .9
                    mat[i][j] += .1


def generateobservationalmatrix(observation:str, map:list[list]) ->list[list]:
    rows = len(map)
    cols = len(map[0])

    mat = []
    prob_correct = .9
    prob_wrong = .05

    for i in range(rows):
        for j in range(cols):
            row = []
            if map[i][j] == observation:
                row[j] = prob_correct
            elif map[i][j] == "B":
                row[j] = 0
            else:
                row[j] = prob_wrong
            mat.append(row)



def printmatrix(mat:list[list], rows:int):
    for i in range(rows):
        print(mat[i])



