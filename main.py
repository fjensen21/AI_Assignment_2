import generatemodels
import transitionmodel
import observationmodel
import StateEstimate
def main():
    tm = transitionmodel.TransitionModel()
    om = observationmodel.ObservationModel()
    priorprob = None #TODO: decide how to setup prior prob
    se = StateEstimate.StateEstimate()
    map = [
        ["H", "H", "T"],
        ["N", "N", "N"],
        ["N", "B", "H"]
    ]

    # Register TM Actions
    tm.registerAction("Up", generatemodels.generatetransitionmatrix("Up", map))
    tm.registerAction("Down", generatemodels.generatetransitionmatrix("Down", map))
    tm.registerAction("Right", generatemodels.generatetransitionmatrix("Right", map))
    tm.registerAction("Left", generatemodels.generatetransitionmatrix("Left", map))

    # Register OM
    om.registerObservation("H",generatemodels.generateobservationalmatrix("H", map))
    om.registerObservation("N",generatemodels.generateobservationalmatrix("N", map))
    om.registerObservation("T",generatemodels.generateobservationalmatrix("T", map))

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




