
class TransitionModel:

    models = {}

    def getTransition(self, action:str):
        return self.models[action]

    def registerAction(self, action:str, mat)->None:
        self.models[action] = mat


    def __repr__(self):
        return