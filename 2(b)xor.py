

import numpy as np

print('Enter weights:')
w11 = int(input('Weight w11 = '))
w12 = int(input('Weight w12 = '))
w21 = int(input('Weight w21 = '))
w22 = int(input('Weight w22 = '))
v1 = int(input('Weight v1 = '))
v2 = int(input('Weight v2 = '))

print('Enter Threshold Value:')
theta = int(input('Theta = '))

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])
z = np.array([0, 1, 1, 0])

convergence = False
iterations = 0

while not convergence:
    zin1 = x1 * w11 + x2 * w21
    zin2 = x1 * w12 + x2 * w22

    print("z1 =", zin1)
    print("z2 =", zin2)

    y1 = np.where(zin1 >= theta, 1, 0)
    y2 = np.where(zin2 >= theta, 1, 0)

    yin = y1 * v1 + y2 * v2
    y = np.where(yin >= theta, 1, 0)

    print("yin =", yin)
    print('Output of Net:')
    print("y =", y)
    print("z =", z)

    if np.array_equal(y, z):
        convergence = True
    else:
        iterations += 1
        print("Net is not learning. Enter another set of weights and Threshold value.")
        w11 = int(input("Weight w11 = "))
        w12 = int(input("Weight w12 = "))
        w21 = int(input("Weight w21 = "))
        w22 = int(input("Weight w22 = "))
        v1 = int(input("Weight v1 = "))
        v2 = int(input("Weight v2 = "))
        theta = int(input("Theta = "))

print("McCulloch-Pitts Net for XOR function")
print("Weights of Neuron Z1:")
print("w11 =", w11)
print("w21 =", w21)
print("Weights of Neuron Z2:")
print("w12 =", w12)
print("w22 =", w22)
print("Weights of Neuron Y:")
print("v1 =", v1)
print("v2 =", v2)
print("Threshold value:")
print("theta =", theta)
print("Convergence achieved in", iterations, "iterations.")
