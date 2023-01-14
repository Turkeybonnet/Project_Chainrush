import ChainsawConsultant
import ManagerRushJobs

class RunRushJobs:

    def select_manager(self):
        chainsaw = ChainsawConsultant.ChainsawConsultant()
        # chainsaw = ManagerRushJobs.ManagerRushJobs()
        chainsaw.run_manager()

        # TODO: Implement more managers, default to Chainsaw for now.
        # managerSelect = input("What manager are you rushing?")

projectChainrush = RunRushJobs()
projectChainrush.select_manager()
