import ManagerGlobals as mg
import random

class ManagerRushJobs:
    def __init__(self):
        self.numCogs = 0
        self.phase = 1
        self.jobAmount = 1
        self.cogCap = 4
        self.phaseAmount = 1
        self.cogsWithJobs = {}
        self.cogWeights = {}
        self.managerName = "Prethinker"
        self.jobWeights = {
            1: {1: 100, 2: 100, 3: 100}
        }

    def run_manager(self):
        while True:
            self.get_cogs()
            self.setup_weights()
            self.pick_rush_jobs()
            self.display_jobs()
            self.hold_up()

    def get_cogs(self):
        self.numCogs = 0
        # Make sure to keep asking for an input until it's valid
        while self.numCogs < 1 or self.numCogs > self.cogCap:
            cogs_input = input("How many Cogs are present? (1-%s)\nIf you're in a new phase, type 'phase' or 'p' to rank the phase up. " % self.cogCap)
            # Rank up the phase if we need to
            if cogs_input.lower() in ('phase', 'p'):
                self.phase += 1
                print("%s has reached phase %s!" % (self.managerName, self.phase))
                continue
            # Catch all possible bad inputs like this, it's bad I know
            try:
                self.numCogs = int(cogs_input)
                if self.numCogs < 1 or self.numCogs > self.cogCap:
                    print("Invalid cog amount input.")
            except:
                print("Invalid cog amount input.")

    def setup_weights(self):
        self.cogWeights = {}
        print("Cogs are listed in left to right order.\nYou are in phase %s." % self.phase)
        for cog in range(self.numCogs):
            # Our manager gets a weight of 100 by default, change in specific manager class function.
            if cog == (self.numCogs-1):
                self.cogWeights[self.managerName] = 100
                continue
            # All normal Cogs get a weight of 100 by default
            self.cogWeights["Cog %s" % (cog + 1)] = 100

    def pick_rush_jobs(self):
        jobChanceList = []
        self.jobAmount = 1
        # Let's make our weighted dict a weighted list so random.choice is like a weighted random
        for jobAmount in self.jobWeights[self.phase]:
            if self.jobWeights[self.phase][jobAmount]:
                for chance in range(self.jobWeights[self.phase][jobAmount]):
                    jobChanceList.append(jobAmount)
        self.jobAmount = random.choice(jobChanceList)
        # Make sure we don't try to assign more rush jobs than there are cogs
        if self.jobAmount > self.numCogs:
            self.jobAmount = self.numCogs

        self.cogsWithJobs = {}
        cogChanceList = []
        # Let's make our weighted dict a weighted list so random.choice is like a weighted random
        for cog in list(self.cogWeights):
            self.cogsWithJobs[cog] = "None"
            if self.cogWeights[cog]:
                for chance in range(self.cogWeights[cog]):
                    cogChanceList.append(cog)
        # FINALLY, assigned the jobs.
        for rushJob in range(self.jobAmount):
            validJob = False
            while not validJob:
                cogChoice = random.choice(cogChanceList)
                if self.cogsWithJobs[cogChoice] == "None":
                    self.cogsWithJobs[cogChoice] = random.choice(mg.RushableGags)
                    validJob = True

    def display_jobs(self):
        displayString = "|"
        for cog in list(self.cogsWithJobs):
            cogNameCenter = 12
            rush = self.cogsWithJobs[cog]
            # Make sure to check if the name is too long, if so adjust.
            if len(cog) > cogNameCenter:
                cogNameCenter = len(cog)+2
                rushString = rush.center(cogNameCenter, " ")
            else:
                rushString = rush.center(12, " ")
            displayString += rushString + "|"
        displayString += "\n|"
        for cog in list(self.cogsWithJobs):
            cogNameCenter = 12
            # Make sure to check if the name is too long, if so adjust.
            if len(cog) > cogNameCenter:
                cogNameCenter = len(cog) + 2
                cogString = cog.center(cogNameCenter, " ")
            else:
                cogString = cog.center(12, " ")
            displayString += cogString + "|"
        print(displayString)


    def hold_up(self):
        buffer = input("Press enter when ready to calculate new jobs.")





