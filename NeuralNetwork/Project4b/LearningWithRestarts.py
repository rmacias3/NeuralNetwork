from Testing import testPenData, testCarData, average, stDeviation
"Hello this is the new file"
"work on that"
penAccuracyList = []
carAccuracyList = []
for i in range(5):
    penAccuracyList.append(testPenData(hiddenLayers=[24])[1])
    carAccuracyList.append(testCarData(hiddenLayers=[16])[1])

avgPen = average(penAccuracyList)
stDevPen = stDeviation(penAccuracyList)
maxPen = max(penAccuracyList)

avgCar = average(carAccuracyList)
stDevCar = stDeviation(carAccuracyList)
maxCar = max(carAccuracyList)

print avgPen, "average pen data"
print stDevPen, "standard deviation pen data"
print maxPen, "maximum accuracy pen data"

print avgCar, "average car data"
print stDevCar, "standard deviation car data"
print maxCar, "maximum accuracy car data"
