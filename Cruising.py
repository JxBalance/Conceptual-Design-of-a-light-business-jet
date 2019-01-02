S = 26.29

g = 9.8
M = 9777.5
dt = 60
t = 0
L = 0
v = 260.41

c = 0.0585
k = 15.1

fleft = 2900

alpha = 0.58

while fleft >= 0:
    q = M * g / k
    # q as drag
    p = q/alpha
    # p as propulsion
    finterval = p * c * dt/3600
    M = M - finterval
    fleft = fleft - finterval
    # print(fleft)
    L = L + v * dt
    t = t + dt

print(L)
print(t)
