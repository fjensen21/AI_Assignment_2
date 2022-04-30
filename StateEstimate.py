import transitionmodel
import observationmodel
import numpy

class StateEstimate:

    def __int__(self, tm, om, priorprob):
        self.tm = tm
        self.om = om
        self.priorprob = priorprob

    def executeFiltering(self, actions:list, observations:list):

        def mult(mat1, mat2, dim):

            result = mat1

            for rows in range(dim):

                for columns in range(dim):

                    result[rows][columns] = (mat1[rows][columns]) * (mat2[rows][columns])

            return result

        def norm(mat1, dim):

            result = mat1
            total_sum = 0

            for rows in range(dim):

                for columns in range(dim):

                    total_sum += mat1[rows][columns]

            for rows in range(dim):

                for columns in range(dim):

                    if (total_sum != 0):

                        result[rows][columns] = (mat1[rows][columns]) / (total_sum)

            return result 


        # Go through every action and observation at step k
        size = len(actions)

        # P_k+1 = OM * TM * P_k
        for k in range(size):

            current_prob = self.priorprob


            #-------------------------------------------------------------------------------------
            # Check the action applied at the current step
            if (actions[k] == "Up"):

                # current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Up")) )
                current_prob = mult(self.priorprob, self.tm.getTransition("Up"), 3)

            elif (actions[k] == "Down"):

                # current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Down")) )
                current_prob = mult(self.priorprob, self.tm.getTransition("Down"), 3)

            elif (actions[k] == "Right"):

                # current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Right")) )
                current_prob = mult(self.priorprob, self.tm.getTransition("Right"), 3)

            elif (actions[k] == "Left"):

                # current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Left")) )
                current_prob = mult(self.priorprob, self.tm.getTransition("Left"), 3)

            #-------------------------------------------------------------------------------------
            # Check the observation at the current step
            if (observations[k] == "N"):

                # current_prob = numpy.multiply(current_prob, (self.om.getObservation("N")) )
                current_prob = mult(current_prob, self.om.getObservation("N"), 3)

            elif (observations[k] == "H"):

                # current_prob = numpy.multiply(current_prob, (self.om.getObservation("H")) )
                current_prob = mult(current_prob, self.om.getObservation("H"), 3)

            elif (observations[k] == "T"):

                # current_prob = numpy.multiply(current_prob, (self.om.getObservation("T")) )
                current_prob = mult(current_prob, self.om.getObservation("T"), 3)

            #-------------------------------------------------------------------------------------   
            # Normalize the current probability
            # numpy.linalg.norm(current_prob)
            current_prob = norm(current_prob, 3)
            
            for row in current_prob:
                print(row)

            print("-------------------------------------------------------------")

            self.priorprob = current_prob


        return current_prob
