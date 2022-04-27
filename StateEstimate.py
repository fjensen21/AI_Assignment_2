import transitionmodel
import observationmodel
import numpy

class StateEstimate:

    def __int__(self, tm, om, priorprob):
        self.tm = tm
        self.om = om
        self.priorprob = priorprob

    def executeFiltering(self, actions:list, observations:list):

        # Go through every action and observation at step k
        size = len(actions)

        # P_k+1 = OM * TM * P_k
        for k in range(size):

            current_prob = self.priorprob


            # Check the action applied at the current step
            if (actions[k] == "Up"):

                current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Up")) )

            elif (actions[k] == "Down"):

                current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Down")) )

            elif (actions[k] == "Right"):

                current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Right")) )

            elif (actions[k] == "Left"):

                current_prob = numpy.multiply(self.priorprob, (self.tm.getTransition("Left")) )



            # Check the observation at the current step
            if (observations[k] == "N"):

                current_prob = numpy.multiply(current_prob, (self.om.getObservation("N")) )

            elif (observations[k] == "H"):

                current_prob = numpy.multiply(current_prob, (self.om.getObservation("H")) )

            elif (observations[k] == "T"):

                current_prob = numpy.multiply(current_prob, (self.om.getObservation("T")) )



            # Normalize the current probability
            numpy.linalg.norm(current_prob)
            for row in current_prob:
                print(row)

            print("-------------------------------------------------------------")

            self.priorprob = current_prob


        return current_prob
