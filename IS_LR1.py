import numpy as np


# Определение функции активации (ступенчатая функция)
def step_function(x):
    return 1 if x > 0 else 0


# Определение однослойной нейронной сети
class SimpleNeuralNetwork:
    def __init__(self, input_size):
        # Инициализация случайных весов и смещения
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def forward(self, inputs):
        # Вычисление взвешенной суммы входов и смещения
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        # Применение функции активации (ступенчатой функции)
        output = step_function(weighted_sum)
        return output


# Создание нейронных сетей для операций AND и OR
and_network = SimpleNeuralNetwork(input_size=2)
or_network = SimpleNeuralNetwork(input_size=2)

# Обучение нейронных сетей
# Для операции AND
and_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and_targets = np.array([0, 0, 0, 1])

for i in range(1000):
    for j in range(len(and_inputs)):
        and_output = and_network.forward(and_inputs[j])
        and_error = and_targets[j] - and_output
        and_network.weights += 0.1 * and_error * and_inputs[j]
        and_network.bias += 0.1 * and_error

# Для операции OR
or_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
or_targets = np.array([0, 1, 1, 1])

for i in range(1000):
    for j in range(len(or_inputs)):
        or_output = or_network.forward(or_inputs[j])
        or_error = or_targets[j] - or_output
        or_network.weights += 0.1 * or_error * or_inputs[j]
        or_network.bias += 0.1 * or_error

# Тестирование нейронных сетей
test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print("AND операция:")
for inputs in test_inputs:
    result = and_network.forward(inputs)
    print(f"{inputs[0]} AND {inputs[1]} = {result}")

print("\nOR операция:")
for inputs in test_inputs:
    result = or_network.forward(inputs)
    print(f"{inputs[0]} OR {inputs[1]} = {result}")

print("\nТестовая OR операция:")
inputs1 = np.array([[0, 1], [0, 0], [1, 0], [1, 1], [1, 1], [0, 0]])
for inputs in inputs1:
    result = or_network.forward(inputs)
    print(f"{inputs[0]} OR {inputs[1]} = {result}")