#python3
import sys
import csv
import os
import io

def topsis(inputCSV, weights, impacts, delimiter = ','):
    csvFile = csv.reader(inputCSV, delimiter = delimiter)
    fields = next(csvFile)

    if len(fields) < 3:
        raise ValueError("input csv must have 3 or more columns")

    if not all(isinstance(weight, (int, float)) for weight in weights):
        raise TypeError("weights must be numeric")

    if len(weights) != len(fields) - 1:
        raise ValueError("number of weights must be equal to number of parameters")

    if not all(impact in ['-', '+'] for impact in impacts):
        raise ValueError("all impacts must be either '+' or '-'")

    if len(impacts) != len(fields) - 1:
        raise ValueError("number of impacts must be equal to number of parameters")

    parsedList = []
    tempList = []
    weightedNormalisationDenominators = [0] * (len(fields) - 1)

    for row in csvFile:
        for i in row[1:]:
            try:
                tempList.append(float(i))
            except:
                raise TypeError("all parameter values must be numeric, check row ", row)

        weightedNormalisationDenominators = [i + j**2 for i, j in zip(weightedNormalisationDenominators, tempList)]
        tempList.insert(0, row[0])
        parsedList.append(tempList)
        tempList = []


    weightSum = 0
    weightSum = sum(weights)
    relativeWeights = [i / weightSum for i in weights]
    weightedNormalisationDenominators = [(i ** 0.5) / j for i, j in zip(weightedNormalisationDenominators, relativeWeights)]
    weightedNormalisedMatrix = []

    tempList = [i / j for i, j in zip(parsedList[0][1:], weightedNormalisationDenominators)]
    weightedNormalisedMatrix.append(tempList)
    bestAlternatives = tempList
    worstAlternatives = tempList
    tempList = []

    bestImpactJumpTable = [ min if i == '-' else max for i in impacts]
    worstImpactJumpTable = [ max if i == '-' else min for i in impacts]

    for row in parsedList[1:]:
        tempList = [i / j for i, j in zip(row[1:], weightedNormalisationDenominators)]
        weightedNormalisedMatrix.append(tempList)
        bestAlternatives = [ func(i, j) for i, j, func in zip(bestAlternatives, tempList, bestImpactJumpTable)]
        worstAlternatives = [ func(i, j) for i, j, func in zip(worstAlternatives, tempList, worstImpactJumpTable)]
        tempList = []

    tempSum = 0
    distancesFromWorst = []
    distancesFromBest = []

    for row in weightedNormalisedMatrix:
        tempList = [(i - j) ** 2 for i, j in zip(row, worstAlternatives)]
        tempSum = sum(tempList)
        tempSum = tempSum ** 0.5
        distancesFromWorst.append(tempSum)
        tempList = [(i - j) ** 2 for i, j in zip(row, bestAlternatives)]
        tempSum = sum(tempList)
        tempSum = tempSum ** 0.5
        distancesFromBest.append(tempSum)

    similarityList = [i / (i + j) for i, j in zip(distancesFromWorst, distancesFromBest)]

    sortedSimilarityList = sorted(similarityList, reverse = True)

    rankList = [sortedSimilarityList.index(i) + 1 for i in similarityList]

    parsedList = [ row + [i] + [j] for row, i, j in zip(parsedList, similarityList, rankList)]

    fields = fields + ['Topsis Score'] + ['Rank']

    resultCSV = io.StringIO()
    csvResult = csv.writer(resultCSV, delimiter = delimiter)
    csvResult.writerow(fields)
    csvResult.writerows(parsedList)
    return resultCSV, similarityList, rankList
