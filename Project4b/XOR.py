from NeuralNet import *
examples = ([([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])], [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])])
accuracies = []
accuracy0Layer = buildNeuralNet(examples, weightChangeThreshold=0.00008, hiddenLayerList=[0], maxItr=500)[1]
accuracies.append(('0', accuracy0Layer))
for i in range(1, 80):
    accuracies.append((str(i), buildNeuralNet(examples, weightChangeThreshold=0.00008, hiddenLayerList=[i], maxItr=500)[1]))
    print accuracies[-1]
print accuracies