from Testing import testPenData, testCarData, average, stDeviation
import csv
with open('Pen0.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Data Type', 'Perceptrons', 'Average Accuracy', 'Standard Deviation', 'Maximum Accuracy'])

    for i in range(0, 9):
        penAccuracyList = []
        carAccuracyList = []
        for k in range(5):
            penAccuracyList.append(testPenData(hiddenLayers=[i * 5])[1])
            carAccuracyList.append(testCarData(hiddenLayers=[i * 5])[1])
        avgPen = average(penAccuracyList)
        stDevPen = stDeviation(penAccuracyList)
        maxPen = max(penAccuracyList)

        avgCar = average(carAccuracyList)
        stDevCar = stDeviation(carAccuracyList)
        maxCar = max(carAccuracyList)
        print "writing"
        spamwriter.writerow(['PenData', str(i * 5), str(avgPen), str(stDevPen), str(maxPen)])
        spamwriter.writerow(['Car Data', str(i * 5), str(avgCar), str(stDevCar), str(maxCar)])

