class StateEstimate:

    def __int__(self, tm, om, priorprob):
        self.tm = tm
        self.om = om
        self.priorprob = priorprob

    def executeFiltering(self) -> list[list]:
        return
