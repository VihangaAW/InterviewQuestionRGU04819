import pandas as pd
# Load the excel sheet into a dataframe
df_travel = pd.read_csv('travel.csv')
# Create an array with scores
scoresArray = [0] * len(df_travel)

def Similarity(valueOne, valueTwo, weight, caseAttribute):
    """
    Returns the similarity of two numbers.
    """
    returnValue = 0
    try:
        valueOne = float(valueOne)
        valueTwo = float(valueTwo)
        interval = df_travel[caseAttribute].max() - df_travel[caseAttribute].min()
        returnValue = abs(valueOne - valueTwo) / interval
        return returnValue * weight
    except ValueError:
        print("Similarity() can be only used for numeric values")

def ExactMatch(valueOne, valueTwo, weight):
    """
    Returns a weighted number if the strings are match.
    """
    returnValue = 0
    if valueOne == valueTwo:
        returnValue = 1 * weight
    else:
        returnValue = 0
    return returnValue

def Calculate(holidayTypeValue, holidayTypeWeight, numberOfPersonsValue, numberOfPersonsWeight, reigonValue, reigonWeight,
transportationValue, transportationWeight, durationValue, durationWeight, seasonValue, seasonWeight, accommondationValue, accommondationWeight, hotelValue, hotelWeight):
    """
    Find the nearest case.
    """
    for x in range(len(df_travel)):
        holidayTypeAns = ExactMatch(holidayTypeValue, df_travel["HolidayType"][x], holidayTypeWeight)
        numberOfPersonsAns = Similarity(numberOfPersonsValue, df_travel["NumberOfPersons"][x], numberOfPersonsWeight, "NumberOfPersons")
        reigonAns = ExactMatch(reigonValue, df_travel["Region"][x], reigonWeight)
        transportationAns = ExactMatch(transportationValue, df_travel["Transportation"][x], transportationWeight)
        durationAns = Similarity(durationValue, df_travel["Duration"][x], durationWeight, "Duration")
        seasonAns = ExactMatch(seasonValue, df_travel["Season"][x], seasonWeight)
        accommondationAns = ExactMatch(accommondationValue,  df_travel["Accommodation"][x], accommondationWeight)
        hotelAns = ExactMatch(hotelValue, df_travel["Hotel"][x], hotelWeight)

        scoresArray[x] = holidayTypeAns + numberOfPersonsAns + reigonAns + transportationAns + durationAns + seasonAns + accommondationAns + hotelAns

    print("Price of the nearest case for the given input: " + str(df_travel["Price"][scoresArray.index(max(scoresArray))]))


# Example
#  Following function will output the price of the nearest case
Calculate("City", 1,
          2, 1,
          "Cairo", 1,
          "Plane", 1,
          7, 1,
          "April", 1,
          "ThreeStars", 1,
          "Hotel Victoria-Cairo", 1)
