class ObservationModel:
    models = {}

    def getObservation(self, action: str) -> list[list]:
        return self.models[action]

    def registerObservation(self, action: str, mat: list[list]) -> None:
        self.models[action] = mat

    #TODO: Add To String methods for matrices
