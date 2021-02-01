from time import sleep
import sys

# variables:

startCodes = ["LPL", "BOH"]
airportCodes = []
airportNames = []
startNames = ["Liverpool John Lennon", "Bournmoth International"]
distancesFromLJL = []
distancesFromBI = []
codesEntered = False
aircraftEntered = False
startCode = ""
endCode = ""
typeOfAircraft = ""
runningCostPerSeatPer100km = 0
numOfFirstClassSeats = 0
numOfFirstClassSeatss = ""
numOfSecondClassSeats = 0

# functions:

def Read():
    try:
        f = open("D:\current year 11 project\Airports.txt", "r")
    except:
        f = open("G:\current year 11 project\Airports.txt", "r")
    for x in f:
        airportCodes.append(x[:3])
        a = 0
        for i in range(4, len(x)):
            if x[i] == ",":
                a = i
                break
        airportNames.append(x[4:a])
        b = 0
        for i in range(a + 1, len(x)):
            if x[i] == ",":
                b = i + 1
                break
        distancesFromLJL.append(x[a+2:b-1])
        distancesFromBI.append(x[b:].replace("\n", ""))

def Menu():
    print("Whould you like to: Enter airport details,")
    print("Enter flight details,")
    print("Enter price plan and calculate profit,")
    print("Clear data")
    choice = input("or Quit \n")
    if choice.lower() != "enter airport details" and choice.lower() != "enter flight details" and choice.lower() != "enter price plan and calculate profit" and choice.lower() != "clear data" and choice.lower() != "quit":
        print("you have entered a choice which is not valid\n")
        sleep(0.1)
        Menu()
    else:
        if choice.lower() == "quit":
            sys.exit()
        elif choice.lower() == "enter airport details":
            EnterairportDetails()
        elif choice.lower() == "enter flight details":
            EnterFlightDetails()
        elif choice.lower() == "enter price plan and calculate profit":
            EnterPricePlanAndCalculateProfit()
        elif choice.lower() == "clear data":
            ClearData()

def EnterairportDetails():
    print("Enter the airport code of where you are going from:")
    print("LPL")
    startCode = input("or BOH\n")
    if startCode.upper() != "LPL" and startCode.upper() != "BOH":
        print("The code you have entered is not a valid starting airport code")
        startCode = ""
        Menu()
        return
    print("Enter the airport code of where you are going to:")
    print(airportCodes[0] + ",")
    print(airportCodes[1] + ",")
    print(airportCodes[2] + ",")
    print(airportCodes[3] + ",")
    endCode = input("or " + airportCodes[4] + "\n")
    good = False
    for x in airportCodes:
        if endCode.upper() == x:
            good = True
    if good is False:
            print("The code you have entered is not a valid ending airport code")
            startCode = ""
            endCode = ""
            Menu()
            return
    print("so you are going to", airportNames[airportCodes.index(endCode.upper())], "from ", startNames[startCodes.index(startCode.upper())], "\n")
    codesEntered = True
    Menu()

def EnterFlightDetails():
    print("what type of aircraft is to be used:")
    print("Medium narrow body,")
    print("Large narrow body,")
    typeOfAircraft = input("or Medium wide body\n")
    if typeOfAircraft.lower() != "medium narrow body" and typeOfAircraft.lower() != "large narrow body" and typeOfAircraft.lower() != "medium wide body":
        print("the type of aircraft is invalid")
        typeOfAircraft = ""
        Menu()
        return
    if typeOfAircraft.lower() == "medium narrow body":
        print("Running cost per seat per 100 km: £8")
        runningCostPerSeatPer100km = 8

        print("Maximum flight range (km): 2650")
        maximumFlightRange = 2650

        print("Capacity if all seats are standard-class: 180")
        capacityIfAllSeatsAreStandardClass = 180

        print("Minimum number of first-class seats (if there sre any): 8")
        minimumNumberOfFirstClassSeats = 8

    elif typeOfAircraft.lower() == "large narrow body":
        print("Running cost per seat per 100 km: £7")
        runningCostPerSeatPer100km = 7

        print("Maximum flight range (km): 5600")
        maximumFlightRange = 5600

        print("Capacity if all seats are standard-class: 220")
        capacityIfAllSeatsAreStandardClass = 220

        print("Minimum number of first-class seats (if there sre any): 10")
        minimumNumberOfFirstClassSeats = 10

    elif typeOfAircraft.lower() == "medium wide body":
        print("Running cost per seat per 100 km: £5")
        runningCostPerSeatPer100km = 5

        print("Maximum flight range (km): 4050")
        maximumFlightRange = 4050

        print("Capacity if all seats are standard-class: 406")
        capacityIfAllSeatsAreStandardClass = 406

        print("Minimum number of first-class seats (if there sre any): 14")
        minimumNumberOfFirstClassSeats = 14
        
    while True:
        numOfFirstClassSeatss = input("in numbers how many first-class seats are on the aircraft \n")
        try:
            numOfFirstClassSeats = int(numOfFirstClassSeatss)
        except:
              print("please enter a valid number \n")
              continue
        break
    if numOfFirstClassSeats != 0:
        if numOfFirstClassSeats < minimumNumberOfFirstClassSeats:
            print("the number of first-class seats is less than the minnimum but not zero \n")
            typeOfAircraft = ""
            numOfFirstClassSeats = 0
            Menu()
            return
        if numOfFirstClassSeats > (capacityIfAllSeatsAreStandardClass / 2):
            print("the number of first-class seats is more than the maximum amount \n")
            typeOfAircraft = ""
            numOfFirstClassSeats = 0
            Menu()
            return
    numOfSecondClassSeats = capacityIfAllSeatsAreStandardClass - (numOfFirstClassSeats * 2)
    print("the number of second class seats is ", numOfSecondClassSeats,"\n")
    aircraftEntered = True
    Menu()

def EnterPricePlanAndCalculateProfit():
    if codesEntered == False:
        print("codes arent entered yet \n")
        Menu()
        return
    if aircraftEntered == False:
        print("aircraft type isn't entered yet \n")
        Menu()
        return
    if startCode.upper() == "LPL":
        if typeOfAircraft.lower() ==  "medium narrow body":
            if distancesFromLJL[airportCodes.index(endCode)] > 2650:
                print("the aircraft you have chossen cant go far enough")
                Menu()
                return
        elif typeOfAircraft.lower() ==  "large narrow body":
            if distancesFromLJL[airportCodes.index(endCode)] > 5600:
                print("the aircraft you have chossen cant go far enough")
                Menu()
                return
        elif typeOfAircraft.lower() ==  "large wide body":
            if distancesFromLJL[airportCodes.index(endCode)] > 4050:
                print("the aircraft you have chossen cant go far enough")
                Menu()
                return
    elif startCode.upper() == "BOH":
        if typeOfAircraft.lower() ==  "medium narrow body":
            if distancesFromBI[airportCodes.index(endCode)] > 2650:
                print("the aircraft you have chossen cant go far enough")
                Menu()
                return
        elif typeOfAircraft.lower() ==  "large narrow body":
            if distancesFromBI[airportCodes.index(endCode)] > 5600:
                print("the aircraft you have chossen cant go far enough")
                Menu()
                return
        elif typeOfAircraft.lower() ==  "large wide body":
            if distancesFromBI[airportCodes.index(endCode)] > 4050:
                print("the aircraft you have chossen cant go far enough")
                Menu()
                return
    while True:
        priceOfStandardClassSeat = input("what is the price of a standard-class seat per 100km")
        try:
            priceOfStandardClassSeat = int(priceOfStandardClassSeat)
        except:
            print("pleas enter a valid number")
            continue
        break
    while True:
        priceOfFirstClassSeat = input("what is the price of a first-class seat per 100km")
        try:
            priceOfStandardClassSeat = int(priceOfStandardClassSeat)
        except:
            print("please enter a valid number")
            continue
        break
    if startCode.upper() == "LJL":
        flightCostPerSeat = runningCostPerSeatPer100km * distancesFromBI[airportCodes.index(endCode)] / 100
    else:
        flightCostPerSeat = runningCostPerSeatPer100km * distancesFromLJL[airportCodes.index(endCode)] / 100
    flightCost = flightCostPerSeat * (numOfFirstClassSeats + numOfSecondClassSeats)
    flightIncome = numOfFirstClassSeats * priceOfFirstClassSeat + numOfSecondClassSeats * priceOfStandardClassSeat
    flightProfit = flightIncome - flightCost
    print(flightCostPerSeat)
    print(flightCost)
    print(flightIncome)
    print(flightProfit)
    Menu()

def ClearData():
    startCodes = ["LPL","BOH"]
    airportCodes = []
    airportNames = []
    startNames = ["Liverpool John Lennon","Bournmoth International"]
    distancesFromLJL = []
    distancesFromBI = []
    codesEntered = False
    aircraftEntered = False
    startCode = ""
    endCode = ""
    typeOfAircraft = ""
    runningCostPerSeatPer100km = 0
    numOfFirstClassSeats = 0
    numOfFirstClassSeatss = ""
    numOfSecondClassSeats = 0
    print("")
    Menu()



Read()
Menu()