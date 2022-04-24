
class TransitionModel:

    models = {}

    def getTransition(self, action:str) -> list[list]:
        return self.models[action]

    def registerAction(self, action:str, mat:list[list])->None:
        self.models[action] = mat


    def __repr__(self):
        return