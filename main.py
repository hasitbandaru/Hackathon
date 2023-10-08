year = 0
totalPop = 1000000
civilianGoods = 20
electricity = 20
water = 20
food = 20
civilianFactory = 1
generator = 1
farm = 1
waterTreatmentFacility = 1
trash = 3
carbonEmission = 1
waterContaminated = 2
printPop = None
printCG = None
printElectricity = None
printWater = None
printFood = None
trashYear = (civilianFactory * 2) + (generator + 1) + (farm * 1.25) + (waterTreatmentFacility * .05)
carbonEmissionYear = (civilianFactory * 1) + (generator + 1.5) + (farm * 3) + (waterTreatmentFacility * 1)
waterContaminatedYear = (civilianFactory * 5) + (generator + 5) + (farm * 1) + (waterTreatmentFacility * .05)
civilianSatisfaction = (((civilianGoods / totalPop) * 1 / 4) + ((electricity / totalPop) * 1 / 4) +
                        ((water / totalPop) * 1 / 4) + ((food / totalPop) * 1 / 4))
popChange = totalPop * 0.1
newPop = totalPop + popChange
CGYear = civilianFactory * 10
electricityYear = generator * 15
waterYear = waterTreatmentFacility * 10
foodYear = farm * 15
earthDamaged = (food + trash + carbonEmission + waterContaminated) / 100
CGChange = CGYear - (totalPop / 100000)
electricityChange = electricityYear - (totalPop / 100000)
waterChange = waterYear - (totalPop / 100000)
foodChange = foodYear - (totalPop / 100000)

print("Balancing Act: The City Builder Game")
def instructionIP():
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    instruction = input("Type in 'I' for instructions and 'P' for play(Use upper-case and press enter): ")
    if 'I' in instruction:
        print("In this game you are the ruler of a city with a growing population. You must build factories to generate")
        print("resources for the customer. There are 3 types of resources food, water, and consumer goods. You must")
        print("maintain a good amount of these goods in order to keep your civilian satisfaction high, if it gets too")
        print("low then you lose. The factories you build to produce these goods create pollution as by-products and")
        print("and you must try and keep the by-products as low as possible if not you will also lose. Good luck! \n")
        inputInstruction = input("Type in a capital H and press enter to return to home screen: ")
        if 'H' in inputInstruction:
            homeScreen()
    if 'P' in instruction:
        homeScreen()


def homeScreen():
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print("Welcome to our conservation simulation!")
    print("(R)esources(Will display the available resources you have, and the amount you gained or lost")
    print("(B)uild factories")
    print("(V)iew trash production")
    print("(C)ivillian satisfaction")
    print("(N)ew Year")
    print("(E)nd game")
    screenInput = input("Type in R, B, V, or C depending on which data set you want to view, type N for new year \n"
                        "the simulation and E to end turn and skip to next year: ")
    if 'R' in screenInput:
        showResources()
    if 'B' in screenInput:
        buildFactories()
    if 'V' in screenInput:
        viewTrashProduction()
    if 'C' in screenInput:
        cSatisfaction()
    if 'N' in screenInput:
        newYear()
    if 'E' in screenInput:
        endGame()


def showResources():
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print("The order in which it is displayed is 'current stock, production per year, change over year'")
    print("Total Population: ")
    popChange = totalPop * 0.1
    printPop = str(totalPop) + "; " + str(popChange) + "; " + str(newPop)
    print(printPop)
    print("Civilian Goods: ")
    CGChange = CGYear - (totalPop / 100000)
    printCG = str(civilianGoods) + "; " + str(CGYear) + "; " + str(CGChange)
    print(printCG)
    print("Electricity: ")
    electricityChange = electricityYear - (totalPop / 100000)
    printElectricity = str(electricity) + "; " + str(electricityYear) + "; " + str(electricityChange)
    print(printElectricity)
    print("water: ")
    waterChange = waterYear - (totalPop / 100000)
    printWater = str(water) + "; " + str(waterYear) + "; " + str(waterChange)
    print(printWater)
    print("food: ")
    foodChange = foodYear - (totalPop / 100000)
    printFood = str(food) + "; " + str(foodYear) + "; " + str(foodChange)
    print(printFood)
    resourceInput = input("Type in 'H' if you want to go back to home screen: ")
    if 'H' in resourceInput:
        homeScreen()


def buildFactories():
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print("You can build factories here")
    print("(C)ivilian Factory")
    print("(G)enerator")
    print("(F)arm")
    print("(W)ater Treatement Facility")
    buildInput = input("Type in C, G, F, or W depending on what plant you want to build and type H to return to home: ")
    if 'C' in buildInput:
        print("\n")
        print(
            "---------------------------------------------------------------------------------------------------------")
        # Struggled to edit a global variable locally
        global civilianFactory
        print("Here is the number of civilian factories, type in the number as a positive value or negative value")
        print("depending on if you want to build or destroy")
        currectCF = "This is the current number of Civilian Factories " + str(civilianFactory)
        print(currectCF)
        CFChange = input("Type in number here: ")
        CFChange = int(CFChange)
        civilianFactory += CFChange
        newCF = "Current amount of Civilian Factories: " + str(civilianFactory)
        print(newCF)
        buildInput2 = input("Type 'B' to return to build screen, type 'H' to return to home or type 'C' to check "
                            "civilian satisfaction: ")
        if 'B' in buildInput2:
            buildFactories()
        if 'H' in buildInput2:
            homeScreen()
        if 'C' in buildInput2:
            cSatisfaction()
    if 'G' in buildInput:
        print("\n")
        print(
            "---------------------------------------------------------------------------------------------------------")
        global generator
        print("Here is the number of generators, type in the number as a positive value or negative value")
        print("depending on if you want to build or destroy")
        currectG = "This is the current number of generators " + str(generator)
        print(currectG)
        GChange = input("Type in number here: ")
        GChange = int(GChange)
        generator += GChange
        newG = "Current amount of Civilian Factories: " + str(generator)
        print(newG)
        buildInput2 = input("Type 'B' to return to build screen, type 'H' to return to home or type 'C' to check "
                            "civilian satisfaction: ")
        if 'B' in buildInput2:
            buildFactories()
        if 'H' in buildInput2:
            homeScreen()
        if 'C' in buildInput2:
            cSatisfaction()
    if 'F' in buildInput:
        print("\n")
        print(
            "---------------------------------------------------------------------------------------------------------")
        global farm
        print("Here is the number of farms, type in the number as a positive value or negative value")
        print("depending on if you want to build or destroy")
        currectFarm = "This is the current number of Civilian Factories " + str(farm)
        print(currectFarm)
        farmChange = input("Type in number here: ")
        farmChange = int(farmChange)
        farm += farmChange
        newFarm = "Current amount of Civilian Factories: " + str(farm)
        print(newFarm)
        buildInput2 = input("Type 'B' to return to build screen, type 'H' to return to home or type 'C' to check "
                            "civilian satisfaction: ")
        if 'B' in buildInput2:
            buildFactories()
        if 'H' in buildInput2:
            homeScreen()
        if 'C' in buildInput2:
            cSatisfaction()
    if 'W' in buildInput:
        print("\n")
        print(
            "---------------------------------------------------------------------------------------------------------")
        global waterTreatmentFacility
        print("Here is the number of Water Treatment Facilities, type in the number as a positive value or negative "
              "value depending on if you want to build or destroy")
        currectWTF = "This is the current number of Water Treatment Facilities " + str(waterTreatmentFacility)
        print(currectWTF)
        WTFChange = input("Type in number here: ")
        WTFChange = int(WTFChange)
        waterTreatmentFacility += WTFChange
        newWTF = "Current amount of Civilian Factories: " + str(waterTreatmentFacility)
        print(newWTF)
        buildInput2 = input("Type 'B' to return to build screen, type 'H' to return to home or type 'C' to check "
                            "civilian satisfaction: ")
        if 'B' in buildInput2:
            buildFactories()
        if 'H' in buildInput2:
            homeScreen()
        if 'C' in buildInput2:
            cSatisfaction()
    if 'H' in buildInput:
        homeScreen()
    if 'C' in buildInput:
        cSatisfaction()


def viewTrashProduction():
    print("\n")
    print(
        "---------------------------------------------------------------------------------------------------------")
    global trashYear
    global carbonEmissionYear
    global waterContaminatedYear
    global earthDamaged
    trashYear = (civilianFactory * 2) + (generator * .1) + (farm * 1.25) + (waterTreatmentFacility * .05)
    carbonEmissionYear = (civilianFactory * 1) + (generator * 1.5) + (farm * 3) + (waterTreatmentFacility * 1)
    waterContaminatedYear = (civilianFactory * .5) + (generator * .5) + (farm * 1) + (waterTreatmentFacility * .05)
    printTrash = "We have produced " + str(trashYear) + " units of trash"
    printCE = "We have produced " + str(carbonEmissionYear) + " units of carbon emissions"
    printWC = "We have produced " + str(waterContaminatedYear) + " units of contaminated water"
    printED = "We have destroyed" + str(earthDamaged) + "% of the Earth, if this number reaches above 50& then we lose"
    print(printTrash)
    print(printCE)
    print(printWC)
    trashInput = input("Press 'H' to return to home screen: ")
    if 'H' in trashInput:
        homeScreen()


def cSatisfaction():
    print("\n")
    print(
        "---------------------------------------------------------------------------------------------------------")
    print("Here you can view the civilian satisfaction of your country and what factories you may need to build")
    print("The highest rating of satisfaction you can get is 1 except for 'Total Satisfaction' which is 4")
    print("If the Total Satisfaction dips below a 3 then you lose, if any of the other ratings fall below one then you")
    print("where you need to build more factories \n")
    global civilianGoods
    global totalPop
    global CGSatisfaction
    global eSatisfaction
    global electricity
    global wSatisfaction
    global water
    global fSatisfaction
    global food

    CGSatisfaction = civilianGoods / (totalPop / 100000)
    if CGSatisfaction >= 1:
        CGSatisfaction = 1
    else:
        CGSatisfaction = civilianGoods / (totalPop / 100000)
    printCGS = "Consumer Goods Satisfaction: " + str(CGSatisfaction)
    print(printCGS)

    eSatisfaction = electricity / (totalPop / 100000)
    if eSatisfaction >= 1:
        eSatisfaction = 1
    else:
        eSatisfaction = electricity / (totalPop / 100000)
    printE = "Electricity Satisfaction: " + str(eSatisfaction)
    print(printE)

    wSatisfaction = water / (totalPop / 100000)
    if wSatisfaction >= 1:
        wSatisfaction = 1
    else:
        wSatisfaction = water / (totalPop / 100000)
    printW = "Water Satisfaction: " + str(wSatisfaction)
    print(printW)

    fSatisfaction = food / (totalPop / 100000)
    if fSatisfaction >= 1:
        fSatisfaction = 1
    else:
        fSatisfaction = food / (totalPop / 100000)
    printF = "Food Satisfaction: " + str(fSatisfaction)
    print(printF)
    global totalSatisfaction
    totalSatisfaction = CGSatisfaction + eSatisfaction + wSatisfaction + fSatisfaction
    TSPrint = "The total satisfaction: " + str(totalSatisfaction)
    print(TSPrint)
    satisfactionInput = input("\nType in 'H' here to return to home or type in 'B' to build factories: ")
    if 'H' in satisfactionInput:
        homeScreen()
    if 'B' in satisfactionInput:
        buildFactories()


def newYear():
    print("\n")
    print(
        "---------------------------------------------------------------------------------------------------------")
    if civilianSatisfaction < 3 or earthDamaged > 50/100:
        endGame()
    else:
        print("Welcome to a new year!")
        global year
        year += 1
        printYear = "This is year #" + str(year) + ", congrats on surviving this far!"
        print(printYear)
        updateResources()
        homeScreen()

def updateResources():
    global totalPop
    global trashYear
    global carbonEmissionYear
    global waterContaminatedYear
    global civilianSatisfaction
    global earthDamaged
    global CGChange
    global electricityChange
    global waterChange
    global foodChange
    trashYear = (civilianFactory * 2) + (generator + 1) + (farm * 1.25) + (waterTreatmentFacility * .05)
    carbonEmissionYear = (civilianFactory * 1) + (generator + 1.5) + (farm * 3) + (waterTreatmentFacility * 1)
    waterContaminatedYear = (civilianFactory * 5) + (generator + 5) + (farm * 1) + (waterTreatmentFacility * .05)
    civilianSatisfaction = (((civilianGoods / totalPop) * 1 / 4) + ((electricity / totalPop) * 1 / 4) +
                            ((water / totalPop) * 1 / 4) + ((food / totalPop) * 1 / 4))
    popChange = totalPop * 0.1
    newPop = totalPop + popChange
    totalPop = newPop
    CGYear = civilianFactory * 10
    electricityYear = generator * 15
    waterYear = waterTreatmentFacility * 10
    foodYear = farm * 15
    earthDamaged = (food + trash + carbonEmission + waterContaminated) / 100
    CGChange = CGYear - (totalPop / 100000)
    electricityChange = electricityYear - (totalPop / 100000)
    waterChange = waterYear - (totalPop / 100000)
    foodChange = foodYear - (totalPop / 100000)

def endGame():
    print("\n")
    print(
        "---------------------------------------------------------------------------------------------------------")
    print("The game has ended!")
    printResources = "Here are the resources: \n CivilianGoods: " + str(civilianGoods) + "\n Electricity: " + str(
        electricity) + "\n Water: " + str(water) + "\n Food: " + str(food)
    print(printResources)
    printFactory = "Here are the factories: \n CivilianGood Factories: " + str(
        civilianFactory) + "\n Generator: " + str(generator) + "\n Water Treatment Facility: " + str(
        waterTreatmentFacility) + "\n Farm: " + str(farm)
    print(printFactory)
    printTrash = "Here is the waste produced: \n Trash: " + str(trash) + "\n Contaminated Water: " + str(
        waterContaminated) + "\n Carbon Emissions: " + str(carbonEmission)
    print(printTrash)
    printCivilianSatisfaction = "Here is the civilian satisfaction: " + str(civilianSatisfaction)
# Struggled to get the end game function to work
instructionIP()



