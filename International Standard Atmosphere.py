import math

print("       ****  ISA  Calculator  Troposhpere  ****")
print()
print("1.Calculate ISA for altitude in meters")
print("2.Calculate ISA for altitude in feets")
print("3.Calculate ISA for altitude in FL")
ch=int(input("Enter your Choice: "))
#hh=float(input("Enter altitude:"))

g0=9.80665
r=287.0
t0=288.15
p0=101325.0
h0=0
d0=1
den0=1.293

if ch==1:
    print("Now begin to calculate")
    hh=float(input("Enter altitude:"))
    h=hh
elif ch==2:
    print("Now begin to calculate")
    hh=float(input("Enter altitude:"))
    h=hh*0.3048
elif ch==3:
    print("Now begin to calculate")
    hh=float(input("Enter altitude:"))
    h=hh*30.48
else:
    print("incorrect input")


if h<=11000:
    h1=h
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    print("Temperature:",t1,"K (",t1-273," 'C)")
    p1=p0*(t1/t0)**(-g0/a1/r)
    per1=p1/p0*100
    print("Pressure:  ",p1,"Pa (",per1," % SL)")
    den1=p1/r/t1
    pd1=den1/den0*100
    print("Density:   ",den1,"Kg/m3 (",pd1," % SL)")
elif  11000<h<=20000:
    h2=h
    h1=11000
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    a2=0
    t2=t1+a2*(h2-h1)
    print("Temperature:",t2,"K (",t2-273," 'C)")
    p1=p0*(t1/t0)**(-g0/(a1*r))
    p2=p1*math.exp(-g0*(h2-h1)/r/t2)
    per2=p2/p0*100
    print("Pressure:  ",p2,"Pa (",per2," % SL)")
    den2=p2/r/t2
    pd2=den2/den0*100  
    print("Density:   ",den2,"Kg/m3 (",pd2," % SL)")
elif  20000<h<=32000:
    h3=h
    h1=11000
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    a2=0
    h2=20000 
    t2=t1+a2*(h2-h1)
    a3=0.0010
    t3=t2+a3*(h3-h2)
    print("Temperature:",t3,"K (",t3-273," 'C)")
    p1=p0*(t1/t0)**(-g0/(a1*r))
    p2=p1*math.exp(-g0*(h2-h1)/r/t2)
    p3=p2*(t3/t2)**(-g0/(a3*r))
    per3=p3/p0*100
    print("Pressure:  ",p3,"Pa (",per3," % SL)")
    den3=p3/r/t3
    pd3=den3/den0*100
    print("Density:   ",den3,"Kg/m3 (",pd3," % SL)")
elif  32000<h<=47000:
    h1=11000
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    a2=0
    h2=20000
    t2=t1+a2*(h2-h1)
    a3=0.0010
    h3=32000
    t3=t2+a3*(h3-h2)
    a4=0.0028
    h4=h
    t4=t3+a4*(h4-h3)
    print("Temperature:",t4,"K (",t4-273," 'C)")
    p1=p0*(t1/t0)**(-g0/(a1*r))
    p2=p1*math.exp(-g0*(h2-h1)/r/t2)
    p3=p2*(t3/t2)**(-g0/(a3*r))
    p4=p3*(t4/t3)**(-g0/(a4*r))
    per4=p4/p0*100
    print("Pressure:  ",p4,"Pa (",per4," % SL)")
    den4=p4/r/t4
    pd4=den4/den0*100
    print("Density:   ",den4,"Kg/m3 (",pd4," % SL)")
elif  47000<h<=51000:
    h1=11000
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    a2=0
    h2=20000
    t2=t1+a2*(h2-h1)
    a3=0.0010
    h3=32000
    t3=t2+a3*(h3-h2)
    a4=0.0028
    h4=47000
    t4=t3+a4*(h4-h3)
    h5=h
    a5=0
    t5=t4+a5*(h5-h4)
    print("Temperature:",t5,"K (",t5-273," 'C)")
    p1=p0*(t1/t0)**(-g0/(a1*r))
    p2=p1*math.exp(-g0*(h2-h1)/r/t2)
    p3=p2*(t3/t2)**(-g0/(a3*r))
    p4=p3*(t4/t3)**(-g0/(a4*r))
    p5=p4*math.exp(-g0*(h5-h4)/r/t5)
    per5=p5/p0*100
    print("Pressure:  ",p5,"Pa (",per5," % SL)")
    den5=p5/r/t5
    pd5=den5/den0*100
    print("Density:   ",den5,"Kg/m3 (",pd5," % SL)")
elif  51000<h<=71000:
    h1=11000
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    a2=0
    h2=20000
    t2=t1+a2*(h2-h1)
    a3=0.0010
    h3=32000
    t3=t2+a3*(h3-h2)
    a4=0.0028
    h4=47000
    t4=t3+a4*(h4-h3)
    h5=51000
    a5=0
    t5=t4+a5*(h5-h4)
    h6=h
    a6=-0.0028
    t6=t5+a6*(h6-h5)
    print("Temperature:",t6,"K (",t6-273," 'C)")
    p1=p0*(t1/t0)**(-g0/(a1*r))
    p2=p1*math.exp(-g0*(h2-h1)/r/t2)
    p3=p2*(t3/t2)**(-g0/(a3*r))
    p4=p3*(t4/t3)**(-g0/(a4*r))
    p5=p4*math.exp(-g0*(h5-h4)/r/t5)
    p6=p5*(t6/t5)**(-g0/(a6*r))
    per6=p6/p0*100
    print("Pressure:  ",p6,"Pa (",per6," % SL)")
    den6=p6/r/t6
    pd6=den6/den0*100
    print("Density:   ",den6,"Kg/m3 (",pd6," % SL)")
elif  71000<h<=86000:
    h1=11000
    a1=-0.0065
    t1=t0+a1*(h1-h0)
    a2=0
    h2=20000
    t2=t1+a2*(h2-h1)
    a3=0.0010
    h3=32000
    t3=t2+a3*(h3-h2)
    a4=0.0028
    h4=47000
    t4=t3+a4*(h4-h3)
    h5=51000
    a5=0
    t5=t4+a5*(h5-h4)
    h6=71000
    a6=-0.0028
    t6=t5+a6*(h6-h5)
    h7=h
    a7=-0.0020
    t7=t6+a7*(h7-h6)
    print("Temperature:",t7,"K (",t7-273," 'C)")
    p1=p0*(t1/t0)**(-g0/(a1*r))
    p2=p1*math.exp(-g0*(h2-h1)/r/t2)
    p3=p2*(t3/t2)**(-g0/(a3*r))
    p4=p3*(t4/t3)**(-g0/(a4*r))
    p5=p4*math.exp(-g0*(h5-h4)/r/t5)
    p6=p5*(t6/t5)**(-g0/(a6*r))
    p7=p6*(t7/t6)**(-g0/(a7*r))
    per7=p7/p0*100
    print("Pressure:  ",p7,"Pa (",per7," % SL)")
    den7=p7/r/t7
    pd7=den7/den0*100
    print("Density:   ",den7,"Kg/m3 (",pd7," % SL)")
elif  86000<h:
    print("beyond computer capacity")
else:
    print("incorret inpout")

dummy=input("Press Enter")
