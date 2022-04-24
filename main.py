import transitionmodel
import observationmodel
def main():
    tm = transitionmodel.TransitionModel()
    om = observationmodel.ObservationModel()
    priorprob = None #TODO: decide how to setup prior prob

    # Register TM Actions
    up = [
        [1.9,1.9,1.9],
        [1,1,1],
        [0.1,0.1,0.1]
    ]
    down = [
        [0.1, 0.1, 0.1],
        [1, 1, 1],
        [1.9, 1.9, 1.9]
    ]
    right = [
        [0.1, 1, 1.9],
        [0.1, 1, 1.9],
        [0.1, 1, 1.9],
    ]
    left = [
        [1.9, 1, 0.1],
        [1.9, 1, 0.1],
        [1.9, 1, 0.1],
    ]
    tm.registerAction("Up", up)
    tm.registerAction("Down", down)
    tm.registerAction("Right", right)
    tm.registerAction("Left", left)

    # Register OM


