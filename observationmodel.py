class ObservationModel:
    models = {}

    def getObservation(self, action: str):
        return self.models[action]

    def registerObservation(self, action: str, mat) -> None:
        self.models[action] = mat

    #TODO: Add To String methods for matrices
