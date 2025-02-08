u = 1.2
d = 1 / u
N = 5
r = 0
K = 45
S0 = 45

# Risk-neutral probability
q = (1 - d) / (u - d)

# Initialize terminal payoff
values = []
for j in range(N + 1):
    S = S0 * (u ** j) * (d ** (N - j))
    payoff = max(S - K, 0)
    values.append(payoff)

# Backward induction
for t in range(N - 1, -1, -1):
    new_values = []
    for j in range(t + 1):
        cont = q * values[j + 1] + (1 - q) * values[j]  # Continuation value
        S = S0 * (u ** j) * (d ** (t - j))              # Current stock price
        intrinsic = max(S - K, 0)                        # Intrinsic value
        new_values.append(max(intrinsic, cont))
    values = new_values

# Calculate Delta_2^dd
# At t=2, after two downward movements (dd), the stock price is S0 * d^2
S_dd = S0 * (d ** 2)
# Option values at t=3 after dd: one more down (ddd) and one up (ddu)
S_ddd = S_dd * d
S_ddu = S_dd * u
# Option values at t=3
value_ddd = max(S_ddd - K, 0)
value_ddu = max(S_ddu - K, 0)
# Delta_2^dd is (value_ddu - value_ddd) / (S_ddu - S_ddd)
Delta_2_dd = (value_ddu - value_ddd) / (S_ddu - S_ddd)

print("Delta_2^dd is:", Delta_2_dd)
