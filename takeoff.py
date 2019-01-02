den_air= 1.225
S=26.29
cltakeoff=1.811
G= 100312.8
p= 35123.2
g=9.8
M=10236

v0=0
vt=63

cd= 0.025
f= 0.1811

dt=0.01
t=0
l=0
v=0

while v<=vt:
   a=(p-0.5*cd*v**2*S*den_air-(G-0.5*cltakeoff*den_air*v**2*S)*f)/M
   #a=den_air/M
   v=v+a*dt
   l=l+v*dt
   t=t+dt

print(l)
print(t)
print(a)
