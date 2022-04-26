import transitionmodel
import observationmodel
import StateEstimate
def main():
    tm = transitionmodel.TransitionModel()
    om = observationmodel.ObservationModel()
    priorprob = None #TODO: decide how to setup prior prob
    se = StateEstimate.StateEstimate()

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
    h = [
        [.9,.9,.05],
        [.05,.05,.05],
        [.05,0,.9]
    ]
    t = [
        [.05,.05,.9],
        [.05,.05,.05],
        [.05,0,.05]
    ]
    n = [
        [.05,.05,.05],
        [.9,.9,.9],
        [.9,0,.05]
    ]
    om.registerObservation("H",h)
    om.registerObservation("N",n)
    om.registerObservation("T",t)

    # Setup Prior Probability
    pp = [
        [.0111,.0111,.0111],
        [.0111, .0111, .0111],
        [.0111, .0111, .0111]
    ]

    # Generate Results
    actions = ["Right","Right","Down","Down"]
    observations = ["N","N","H","H"]
    se.tm = tm
    se.om = om
    se.priorprob = pp
    prob_distribution = se.executeFiltering(actions, observations)

    #TODO: Somehow print this matrix




