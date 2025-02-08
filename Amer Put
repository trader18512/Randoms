u = 1.5
d = 1 / u
N = 50
r = 0
K = 45
S0 = 45

# Risk-neutral probability
q = (1 - d) / (u - d)

# Initialize terminal payoff
values = []
for j in range(N + 1):
    S = S0 * (u ** j) * (d ** (N - j))
    payoff = max(K - S, 0)
    values.append(payoff)

# Backward induction
for t in range(N - 1, -1, -1):
    new_values = []
    for j in range(t + 1):
        cont = q * values[j + 1] + (1 - q) * values[j]  # Continuation value
        S = S0 * (u ** j) * (d ** (t - j))              # Current stock price
        intrinsic = max(K - S, 0)                        # Intrinsic value
        new_values.append(max(intrinsic, cont))
    values = new_values

print("The price of the American put is:", values[0])
