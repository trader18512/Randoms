import numpy as np

# Parameters
u = 1.5
d = 1/u
T = 50
N = T
r = 0
K = 45
S_0 = 45

# Risk-neutral probability
p = (np.exp(r) - d) / (u - d)

# Binomial tree
stock_price = np.zeros((N+1, N+1))
option_value = np.zeros((N+1, N+1))

# Compute stock prices at each node
for i in range(N+1):
    for j in range(i+1):
        stock_price[j, i] = S_0 * (u**(i-j)) * (d**j)

# Compute option value at maturity
for j in range(N+1):
    option_value[j, N] = max(0, stock_price[j, N] - K)

# Backward induction
for i in range(N-1, -1, -1):
    for j in range(i+1):
        option_value[j, i] = max(stock_price[j, i] - K, (p * option_value[j, i+1] + (1-p) * option_value[j+1, i+1]) * np.exp(-r))

# Option price at t=0
option_price = option_value[0, 0]

print(f"The price of the American call option is: {option_price:.2f}")
