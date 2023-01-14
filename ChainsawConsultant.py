import ManagerGlobals as mg
import ManagerRushJobs

class ChainsawConsultant(ManagerRushJobs.ManagerRushJobs):
    def __init__(self):
        ManagerRushJobs.ManagerRushJobs.__init__(self)
        self.cogCap = 5
        self.phaseAmount = 3
        self.managerName = "Chainsaw"
        self.jobWeights = {
            1: mg.PhaseOneJobAmountWeights,
            2: mg.PhaseTwoJobAmountWeights,
            3: mg.PhaseThreeJobAmountWeights
        }

    def setup_weights(self):
        self.cogWeights = {}
        print("Cogs are listed in left to right order.\nYou are in phase %s." % self.phase)
        for cog in range(self.numCogs):
            if cog == (self.numCogs-1):
                self.cogWeights[self.managerName] = 100
                if self.phase == 2:
                    self.cogWeights[self.managerName] -= mg.PhaseTwoChainsawWeightReduction
                continue
            self.cogWeights["Cog %s" % (cog + 1)] = 100
            if self.phase in (1, 3):
                isCTS = input("Is Cog %s a CUT THE SLACK Cog? (y/n) " % (cog+1))
                if isCTS.lower() == 'y':
                    if self.phase == 1:
                        self.cogWeights["Cog %s" % (cog+1)] += mg.PhaseOneCTSTargetWeightBonus
                    else:
                        self.cogWeights["Cog %s" % (cog+1)] += mg.PhaseThreeCTSTargetWeightBonus
                else:
                    continue





