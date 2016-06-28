from Testing import testPenData, testCarData, average, stDeviation
import csv
with open('Pen0.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Data Type', 'Perceptrons', 'Average Accuracy', 'Standard Deviation', 'Maximum Accuracy'])
    penAccuracyList = []
    carAccuracyList = []
    for k in range(5):
        penAccuracyList.append(testPenData(hiddenLayers=[])[1])
        #carAccuracyList.append(testCarData(hiddenLayers=[])[1])
    avgPen = average(penAccuracyList)
    stDevPen = stDeviation(penAccuracyList)
    maxPen = max(penAccuracyList)
    spamwriter.writerow(['PenData', '0', str(avgPen), str(stDevPen), str(maxPen)])
"""
    avgCar = average(carAccuracyList)
    stDevCar = stDeviation(carAccuracyList)
    maxCar = max(carAccuracyList)
    print "writing"
"""

    #spamwriter.writerow(['Car Data', '0', str(avgCar), str(stDevCar), str(maxCar)])
