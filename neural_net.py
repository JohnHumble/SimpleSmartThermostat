import numpy as np

def sigmoid(x):
    # Sigmoid activation function: 
    return 1 / (1 + np.exp(-x))

class NeuronLayer:
    """ basic layer of neurons """
    def __init__(self, num_neurons, num_weights):
        self.num_neurons = num_neurons
        self.neurons = np.zeros(self.num_neurons)

        # weights are stored as follows w[in_val, neuron]
        self.num_weights = num_weights
        
        self.init_weights()
        self.init_bias()

    def init_weights(self):
        self.weights = np.zeros((self.num_weights, self.num_neurons))
        # initialize weights as random
        for i in range(self.num_weights):
            for j in range(self.num_neurons):
                self.weights[i, j] = np.random.normal()
    
    def init_bias(self):
        self.bias = np.zeros(self.num_neurons)
        # initialize biases as random
        for i in range(self.num_neurons):
            self.bias = np.random.normal()

    def update(self, layer):
        # update the values in the layer for each one
        for i in range(self.num_neurons):
            w = self.weights[:, i]
            neurons[i] = sigmoid(np.sum(np.multiply(w, layer) + self.bias[i]))
    def get_values(self):
        return self.neurons

class NeuralNet:
    """
    A basic Neural Network with a specified amount of of inputs, layers, and nodes
    """
    def __init__(self, num_in, num_out, hidden):
        
        # inputs
        self.in_vec = np.zeros(num_in)
        num_weights = num_in

        # hidden layer
        self.hidden = []
        for i in range(len(hidden)):
            hidden.append(NeuronLayer(hidden[i], num_weights))
            num_weights = hidden[i]

        # output layer
        self.out = NeuronLayer(hidden[i], num_weights)

    def get_output(self):
        return self.out.get_values()

    def train(self, in_data, true_out, epochs=1000, learn_rate=0.1):
        
        # apply the method
        for epoch in range(epochs):
            for x, y_true in zip(in_data, true_out):
                self.feed_forward(x)

                # TODO put system here for backtracking and updating weights and biases of nodes


    def feed_forward(self, in_vec):
        self.in_vec = in_vec
        prev = in_vec
        for i in range(len(self.hidden)):
            self.hidden[i].update(prev)
            prev = self.hidden[i].get_values()
        self.out.update(prev)