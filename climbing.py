import math

G = 100312.8
p = 35123.2
g = 9.8
M = 10236
S=26.29

def denair(h):
    
    g0=9.80665
    r=287.0
    t0=288.15
    p0=101325.0
    h0=0
    den0=1.293
    
    den=0

    if h<=11000:
        h1=h
        a1=-0.0065
        t1=t0+a1*(h1-h0)

        p1=p0*(t1/t0)**(-g0/a1/r)
        per1=p1/p0*100

        den1=p1/r/t1
        pd1=den1/den0*100
        den=den1

    
    elif  11000<h<=20000:
        h2=h
        h1=11000
        a1=-0.0065
        t1=t0+a1*(h1-h0)
        a2=0
        t2=t1+a2*(h2-h1)
        p1=p0*(t1/t0)**(-g0/(a1*r))
        p2=p1*math.exp(-g0*(h2-h1)/r/t2)
        per2=p2/p0*100
        den2=p2/r/t2
        pd2=den2/den0*100  
        den=den2

    return den

def soundspeed(h):
        
    g0=9.80665
    r=287.0
    t0=288.15
    p0=101325.0
    h0=0
    den0=1.293
    
    c=0

    den=0

    if h<=11000:
        h1=h
        a1=-0.0065
        t1=t0+a1*(h1-h0)
        p1=p0*(t1/t0)**(-g0/a1/r)
        per1=p1/p0*100
        den1=p1/r/t1
        pd1=den1/den0*100
        den=den1
        c=math.sqrt(1.4*t1*287)

    
    elif  11000<h<=20000:
        h2=h
        h1=11000
        a1=-0.0065
        t1=t0+a1*(h1-h0)
        a2=0
        t2=t1+a2*(h2-h1)
        p1=p0*(t1/t0)**(-g0/(a1*r))
        p2=p1*math.exp(-g0*(h2-h1)/r/t2)
        per2=p2/p0*100
        den2=p2/r/t2
        pd2=den2/den0*100  
        den=den2
        c=math.sqrt(1.4*t2*287)

    return c

kp=0

def propulsion(h):
   kp=h/13000
   p=kp*(1225-1050)+1050 
   return p


kf=0
def fuelconsumption(h):
    kf=h/13000
    f=kf*(0.0351-0.0345)+0.045
    return f

def clalpha(v):
    ma=v/soundspeed(h)
    clalpha=(6.0186-3.9105)/0.9*ma
    return clalpha

v2=63.31

h=10.7

ma=0
v=128

L=0
vy=0
alpha=0
rld=12

dt=10

while h<=13000:
    ma=v/soundspeed(h)
    p=propulsion(h)*2*g
    G=G-fuelconsumption(h)*dt*p
    L=G
    Q=L/rld
    cl=L*2/denair(h)/S/v**2
    cla=clalpha(v)
    alpha=(cl-0.3194)/cla
    vy=(p*math.cos(alpha)-Q)*v/G
    print(h,vy,alpha/3.14*180)
    h=h+vy*dt





