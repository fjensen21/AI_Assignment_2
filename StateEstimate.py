import transitionmodel
import observationmodel
import numpy

class StateEstimate:

    def __int__(self, tm, om, priorprob):
        self.tm = tm
        self.om = om
        self.priorprob = priorprob

    def executeFiltering(self, actions:list, observations:list, total_rows, total_columns):

        def mult(mat1, mat2, total_rows, total_columns):

            result = mat1

            for rows in range(total_rows):

                for columns in range(total_columns):

                    result[rows][columns] = (mat1[rows][columns]) * (mat2[rows][columns])

            return result

        def norm(mat1, total_rows, total_columns):

            result = mat1
            total_sum = 0

            for rows in range(total_rows):

                for columns in range(total_columns):

                    total_sum += mat1[rows][columns]

            for rows in range(total_rows):

                for columns in range(total_columns):

                    if (total_sum != 0):

                        result[rows][columns] = (mat1[rows][columns]) / (total_sum)

            return result 


        # Go through every action and observation at step k
        size = len(actions)

        # P_k+1 = OM * TM * P_k
        for k in range(size):

            # print("Step: {}".format(k + 1))

            current_prob = self.priorprob


            #-------------------------------------------------------------------------------------
            # Check the action applied at the current step
            if (actions[k] == "Up"):

                current_prob = mult(self.priorprob, self.tm.getTransition("Up"), total_rows, total_columns)

            elif (actions[k] == "Down"):

                current_prob = mult(self.priorprob, self.tm.getTransition("Down"), total_rows, total_columns)

            elif (actions[k] == "Right"):

                current_prob = mult(self.priorprob, self.tm.getTransition("Right"), total_rows, total_columns)

            elif (actions[k] == "Left"):

                current_prob = mult(self.priorprob, self.tm.getTransition("Left"), total_rows, total_columns)

            #-------------------------------------------------------------------------------------
            # Check the observation at the current step
            if (observations[k] == "N"):

                current_prob = mult(current_prob, self.om.getObservation("N"), total_rows, total_columns)

            elif (observations[k] == "H"):

                current_prob = mult(current_prob, self.om.getObservation("H"), total_rows, total_columns)

            elif (observations[k] == "T"):

                current_prob = mult(current_prob, self.om.getObservation("T"), total_rows, total_columns)

            #-------------------------------------------------------------------------------------   
            # Normalize the current probability
            current_prob = norm(current_prob, total_rows, total_columns)
            


            # for row in current_prob:
            #     print(row)

            # print("-------------------------------------------------------------")

            self.priorprob = current_prob


        return current_prob
