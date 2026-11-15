import numpy as np


def sigmoid(z):
    return 1/(1+np.exp(-z))


def digit_network_forward(image, weights, biases):
    """Run an image through a fully connected sigmoid network.

    Returns (output activations rounded to 4 decimals, predicted digit).
    """
    inputs = []
    for row in image:
        inputs.extend(row)
    
    result = inputs
    for w, b in zip(weights, biases):
        temp_res = []
        for i in range(len(w)):
            temp = sigmoid(sum([x*y for x, y in zip(result, w[i])])+b[i])
            temp_res.append(temp)
        result = temp_res

    prediction = int(np.argmax(result))
    return [round(float(x), 4) for x in result], np.argmax(result)


       

