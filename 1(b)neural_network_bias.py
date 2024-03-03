# number of elements as input 
n = float(input("Enter number of elements: "))

print("Enter the inputs")
inputs = []
# creating an empty list for inputs3

# iterating till the range
for i in range(0, n):
    ele = float(input())
    inputs.append(ele)  # adding the element
print(inputs)

print("Enter the weights")
# creating an empty list for weights
weights = []
# iterating till the range
for i in range(0, n):
    ele = float(input())
    weights.append(ele)  # adding the element
print(weights)

print("The net input can be calculated as Yin = x1w1 + x2w2 + x3w3")
# creating an empty list for Yin
Yin = []
for i in range(0, n):
    Yin.append(inputs[i] * weights[i])

print(round(sum(Yin), 3))
