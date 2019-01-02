den_air = 1.225
S = 26.29
clland = 0.3
G = 70765.8
p = 1405.3984
g = 9.8
M = 7221

cd = 0.025
f = 0.3

dt = 0.1
t = 0
L = 0
v = 65.791

a = 0.0
N = 0
while v >= 0:
    N = G - 0.5 * clland * den_air * v**2 * S
    if N > 0:
        a = (p - 0.5 * cd * v**2 * S * den_air - N * f) / M
    else:
        a = (p - 0.5 * cd * v**2 * S * den_air) / M
        print(a)
    print(N, a, v)
    # a=den_air/M
    v = v + a * dt
    L = L + v * dt
    t = t + dt

print(L)
print(t)
