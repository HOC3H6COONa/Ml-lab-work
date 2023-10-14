# Импортируем модуль random для генерации случайных чисел
import random

# Задаем обучающие данные для цифр 0-9 в виде списков.
# Эти данные используются для обучения перцептрона.
training_data_0 = list('111101101101111')
training_data_1 = list('001001001001001')
training_data_2 = list('111001111100111')
training_data_3 = list('111001111001111')
training_data_4 = list('101101111001001')
training_data_5 = list('111100111001111')
training_data_6 = list('111100111101111')
training_data_7 = list('111001001001001')
training_data_8 = list('111101111101111')
training_data_9 = list('111101111001111')

# Собираем обучающие данные в список 'numbers'
numbers = [training_data_0, training_data_1, training_data_2, training_data_3, training_data_4, training_data_5, training_data_6, training_data_7, training_data_8, training_data_9]

key = 5
num_pixels = 15

# Инициализируем веса для каждого пикселя в начальный момент времени
weights = [0 for _ in range(num_pixels)]

# Определяем функцию perceptron для классификации цифр на основе данных
def perceptron(pixel_data):
    threshold = 7
    sum_value = 0

    # Суммируем произведения значений пикселей на их веса
    for i in range(num_pixels):
        sum_value += int(pixel_data[i]) * weights[i]

    # Если сумма больше или равна пороговому значению, возвращаем True, иначе False
    if sum_value >= threshold:
        return True
    else:
        return False

# Определяем функции для уменьшения и увеличения весов, в зависимости от результата классификации
def decrease_weights(input_data):
    for i in range(num_pixels):
        if int(input_data[i]) == 1:
            weights[i] -= 1

def increase_weights(input_data):
    for i in range(num_pixels):
        if int(input_data[i]) == 1:
            weights[i] += 1

# Устанавливаем количество итераций обучения
num_iterations = 100000

# Начинаем цикл обучения
for i in range(num_iterations):
    # Генерируем случайное число j для выбора случайной цифры из обучающих данных
    j = random.randint(0, 9)

    # Запускаем перцептрон на выбранной цифре
    result = perceptron(numbers[j])

    # Проверяем, соответствие key
    if j != key:
        # Если результат неверный, уменьшаем веса пикселей
        if result:
            decrease_weights(numbers[j])
    else:
        # Если выбрано смещение и результат неверный, увеличиваем веса пикселей
        if not result:
            increase_weights(numbers[key])

# Выводим полученные веса
print(weights)

# Задаем тестовые данные для проверки работы перцептрона, цифра 5
test_data_1 = list('111100111001110')
test_data_2 = list('111100011001111')
test_data_3 = list('111100111001010')
test_data_4 = list('111100111001101')

# Запускаем перцептрон на тестовых данных и выводим результат
print("Цифра 5 распознана:")
print("1: " + str(perceptron(test_data_1)))
print("2: " + str(perceptron(test_data_2)))
print("3: " + str(perceptron(test_data_3)))
print("4: " + str(perceptron(test_data_4)))
