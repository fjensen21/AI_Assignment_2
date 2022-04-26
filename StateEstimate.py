class StateEstimate:

    def __int__(self, tm, om, priorprob):
        self.tm = tm
        self.om = om
        self.priorprob = priorprob

    def executeFiltering(self, actions:list, observations:list) -> list[list]:
        return
