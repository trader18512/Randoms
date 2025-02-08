import math

# Given parameters
u = 1.2
d = 0.8
T = 5
r = 0.05
K = 52
S0 = 50

# Risk-neutral probabilities
q = (math.exp(r) - d) / (u - d)

# Initialize a binomial tree for option prices
option_tree = [[0 for _ in range(T + 1)] for _ in range(T + 1)]

# Compute option prices at maturity
for i in range(T + 1):
    ST = S0 * (u ** (T - i)) * (d ** i)
    option_tree[T][i] = max(0, ST - K)

# Backward induction to calculate option prices at earlier nodes
for t in range(T - 1, -1, -1):
    for i in range(t + 1):
        option_tree[t][i] = math.exp(-r) * (q * option_tree[t + 1][i] + (1 - q) * option_tree[t + 1][i + 1])

# Delta at the second node in the second period (d2)
delta_2_dd = (option_tree[2][1] - option_tree[2][2]) / (S0 * u * d - S0 * d * d)

print("Delta_2_dd:", delta_2_dd)
