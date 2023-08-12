class bird:
    def __init__(self,primaryColor,wingspan,hasBeak=True):
        self.primaryColor = primaryColor
        self.wingspan = wingspan
        self.hasBeak = hasBeak
    
    def printBirdAttributes(self):
        print(f"This Birds Primary Color is: {self.primaryColor}")
        print(f"This Birds Wingspan is: {self.wingspan}")
        print(f"Does Bird Have Beak?: {self.hasBeak}")

    # This function should increase the bird's wingspan by 1
    def giveBirdGrowthHormonesOneTime(self):
        self.wingspan += 1

    def doesBirdHaveABeak(self):
        print(self.hasBeak)
    
    # TODO: This function will add a beak if the bird does NOT have a beak already.
    def addBeak(self):
        if self.hasBeak == False:
            self.hasBeak = True
      
angryBird = bird("red",0,False)
angryBird.printBirdAttributes()
# bird wingspan is 0
angryBird.giveBirdGrowthHormonesOneTime()
# bird wingspan should now be 1
angryBird.printBirdAttributes()
angryBird.doesBirdHaveABeak()
angryBird.addBeak()
angryBird.printBirdAttributes()



# AlreadyGrownBird = bird("black",5)
# AlreadyGrownBird.printBirdAttributes()
# # bird wingspan is 5
# AlreadyGrownBird.giveBirdGrowthHormonesOneTime()
# # bird wingspan should now be 6
# AlreadyGrownBird.printBirdAttributes()