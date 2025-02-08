import numpy as np

# Parameters
u = 1.5
d = 1/u
T = 5  # N = T
r = 0
K = 31
S0 = 36

# Binomial Tree
dt = 1
q = (1 - d) / (u - d)
binomial_tree = np.zeros((T + 1, T + 1))

# Calculate asset price at each node
for i in range(T + 1):
    for j in range(i + 1):
        binomial_tree[j, i] = S0 * (u ** (i - j)) * (d ** j)

# Calculate option value at each node
option_tree = np.zeros((T + 1, T + 1))
for j in range(T + 1):
    option_tree[j, T] = max(K - binomial_tree[j, T], 0)

# Backward induction to find option price at t=0
for i in range(T - 1, -1, -1):
    for j in range(i + 1):
        option_tree[j, i] = max(K - binomial_tree[j, i], np.exp(-r * dt) * (q * option_tree[j, i + 1] + (1 - q) * option_tree[j + 1, i + 1]))

print("The price of the American put option is:", option_tree[0, 0])
