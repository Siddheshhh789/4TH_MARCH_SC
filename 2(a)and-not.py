# Enter the number of inputs
num_ip = int(input("Enter the number of inputs: "))

# Set the weights with value 1
w1 = 1
w2 = -1  # Assuming w2 as inhibitory

print("For the", num_ip, "inputs, calculate the net input using Yin = x1w1 + x2w2")

x1 = []
x2 = []

for j in range(0, num_ip):
    ele1 = int(input("x1 = "))
    ele2 = int(input("x2 = "))
    x1.append(ele1)
    x2.append(ele2)

print("x1 =", x1)
print("x2 =", x2)

# Calculate net inputs
Yin_excitatory = [x1[i] * w1 + x2[i] * w2 for i in range(num_ip)]
print("Yin (excitatory) =", Yin_excitatory)

Yin_inhibitory = [x1[i] * w1 - x2[i] * w2 for i in range(num_ip)]
print("Yin (inhibitory) =", Yin_inhibitory)

# Firing the neuron based on the threshold
threshold = 1
Y_excitatory = [1 if y >= threshold else 0 for y in Yin_excitatory]
Y_inhibitory = [1 if y >= threshold else 0 for y in Yin_inhibitory]

print("After assuming one weight as excitatory, Y (excitatory) =", Y_excitatory)
print("After assuming one weight as inhibitory, Y (inhibitory) =", Y_inhibitory)
