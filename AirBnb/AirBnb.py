# Define Variables
roomPrice = 100
roomCount = 1
aviableDays = 30
occupanyRate = 0.6

print(f"Room Price is {roomPrice} ")


cleaningFee = 50
unitBill = 5

#Fixed Cost
rent = 2500
maintainance = 500

def CalculateRevenue (roomPrice, roomCount, aviableDays, occupanyRate):
    revenue = roomPrice * roomCount * aviableDays * occupanyRate
    return revenue
    
def calculateVariableCost (roomCount, aviableDays, occupanyRate, cleaningFee, unitBill):
    variableCost = roomCount * aviableDays * occupanyRate *  (cleaningFee + unitBill)
    return variableCost

def calculateFixedCost (rent, maintainance):
    return rent + maintainance

c1 = CalculateRevenue (roomPrice, roomCount, aviableDays, occupanyRate)
c2 = calculateVariableCost (roomCount, aviableDays, occupanyRate, cleaningFee, unitBill)
c3 = calculateFixedCost (rent, maintainance)

def calculateProfit(c1 , c2, c3):
    return c1 - c2 - c3

c4 = calculateProfit(c1 , c2, c3)
print(c1, c2, c3, c4)
