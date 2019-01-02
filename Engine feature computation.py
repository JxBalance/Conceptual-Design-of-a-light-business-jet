# computation preperation
import math

# ploting preperation
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Atmosphere:

    # the method to caculate all the wanted factors
    def allFactors(self, h):

        import math

        g0 = 9.80665
        r = 287.0
        t0 = 288.15
        p0 = 101325.0
        h0 = 0
        den0 = 1.293
        # initial factors

        result_p = 0
        result_p_proportion = 0
        result_t = 0
        result_t_tInK = 0
        result_den = 0
        result_den_proportion = 0
        result_acoustic_speed = 0
        # wanted result factors

        if h <= 11000:
            h1 = h
            a1 = -0.0065
            t1 = t0+a1*(h1-h0)
            #print("Temperature:", t1, "K (", t1-273, " 'C)")
            result_t_tInK = t1

            p1 = p0*(t1/t0)**(-g0/a1/r)
            per1 = p1/p0*100
            #print("Pressure:  ", p1, "Pa (", per1, " % SL)")
            result_p = p1
            result_p_proportion = per1

            den1 = p1/r/t1
            pd1 = den1/den0*100
            #print("Density:   ", den1, "Kg/m3 (", pd1, " % SL)")
            result_den = den1
            result_den_proportion = pd1

        elif 11000 < h <= 20000:
            h2 = h
            h1 = 11000
            a1 = -0.0065
            t1 = t0+a1*(h1-h0)
            a2 = 0
            t2 = t1+a2*(h2-h1)
            #print("Temperature:", t2, "K (", t2-273, " 'C)")
            result_t_tInK = t2

            p1 = p0*(t1/t0)**(-g0/(a1*r))
            p2 = p1*math.exp(-g0*(h2-h1)/r/t2)
            per2 = p2/p0*100
            #print("Pressure:  ", p2, "Pa (", per2, " % SL)")
            result_p = p2
            result_p_proportion = per2

            den2 = p2/r/t2
            pd2 = den2/den0*100
            #print("Density:   ", den2, "Kg/m3 (", pd2, " % SL)")
            result_den = den2
            result_den_proportion = pd2

        elif 20000 < h <= 32000:
            h3 = h
            h1 = 11000
            a1 = -0.0065
            t1 = t0+a1*(h1-h0)
            a2 = 0
            h2 = 20000
            t2 = t1+a2*(h2-h1)
            a3 = 0.0010
            t3 = t2+a3*(h3-h2)
            #print("Temperature:", t3, "K (", t3-273, " 'C)")
            result_t_tInK = t3

            p1 = p0*(t1/t0)**(-g0/(a1*r))
            p2 = p1*math.exp(-g0*(h2-h1)/r/t2)
            p3 = p2*(t3/t2)**(-g0/(a3*r))
            per3 = p3/p0*100
            #print("Pressure:  ", p3, "Pa (", per3, " % SL)")
            result_p = p3
            result_p_proportion = per3

            den3 = p3/r/t3
            pd3 = den3/den0*100
            #print("Density:   ", den3, "Kg/m3 (", pd3, " % SL)")
            result_den = den3
            result_den_proportion = pd3

        elif 32000 < h <= 47000:
            h1 = 11000
            a1 = -0.0065
            t1 = t0+a1*(h1-h0)
            a2 = 0
            h2 = 20000
            t2 = t1+a2*(h2-h1)
            a3 = 0.0010
            h3 = 32000
            t3 = t2+a3*(h3-h2)
            a4 = 0.0028
            h4 = h
            t4 = t3+a4*(h4-h3)
            #print("Temperature:", t4, "K (", t4-273, " 'C)")
            result_t_tInK = t4

            p1 = p0*(t1/t0)**(-g0/(a1*r))
            p2 = p1*math.exp(-g0*(h2-h1)/r/t2)
            p3 = p2*(t3/t2)**(-g0/(a3*r))
            p4 = p3*(t4/t3)**(-g0/(a4*r))
            per4 = p4/p0*100
            #print("Pressure:  ", p4, "Pa (", per4, " % SL)")
            result_p = p4
            result_p_proportion = per4

            den4 = p4/r/t4
            pd4 = den4/den0*100
            #print("Density:   ", den4, "Kg/m3 (", pd4, " % SL)")
            result_den = den4
            result_den_proportion = pd4

        result_t = result_t_tInK-273

        result_acoustic_speed = math.sqrt(1.4*287.1*result_t_tInK)

        return result_p, result_p_proportion, result_t, result_t_tInK, result_den, result_den_proportion, result_acoustic_speed

    # the method to extract the pressure
    def pressure(self, h):
        tem = self.allFactors(h)
        p = tem[0]
        return p

    # the method to extract the proportion of pressure
    def proportion_pressure(self, h):
        tem = self.allFactors(h)
        p = tem[1]
        return p

    # the method to extract the temperature
    def temperature(self, h):
        tem = self.allFactors(h)
        t = tem[2]
        return t

    # the method to extract the temperature in K
    def temperature_ink(self, h):
        tem = self.allFactors(h)
        t = tem[3]
        return t

    # the method to extract the density of the air
    def density(self, h):
        tem = self.allFactors(h)
        den = tem[4]
        return den

    # the method to extract the proportion of the dansity
    def density_proportion(self, h):
        tem = self.allFactors(h)
        den = tem[5]
        return den

    # the method to extract the acoustic speed
    def acoustic_speed(self, h):
        tem = self.allFactors(h)
        aspeed = tem[6]
        return aspeed


# instantiation
atmo = Atmosphere()

# define the thrust value at the sea level
# test value of B787
## thrust_sea_level = 31632
# test value of A320
## thrust_sea_level = 10757
thrust_sea_level = 1792.6


# define the Bypass ratio
ratio_bypass = 4.12

# define the correction coefficient
c = 20

# define the temperature at sea level
t_std = 288.15

# define the pressure at sea level
p_std = 101325.0

# define the SFC at sea level with o speed in kg/N/h
sfc_initial=0.0499


# function to caculate the temperature factor theta with altitude and Ma

def theta(Ma, h):

    # current temperature in K, also known as static temperature
    tink = atmo.temperature_ink(h)

    # static temperature
    t_oat = tink

    # factor theta
    theta0 = t_oat*(1+0.2*Ma**2)/t_std

    return theta0

# function to caculate the pressure factor delta with altitude and Ma


def delta(Ma=0, h=0):
    # current pressure
    pressure = atmo.pressure(h)

    # caculate the delta
    delta = pressure/p_std*(1+0.2*Ma**2)**3.5

    return delta


# function to caculate the current thrust of the given altitude and Ma
def thrust(Ma=0, h=0):

    import math

    theta0 = theta(Ma, h)

    delta0 = delta(Ma, h)

    # throttle ratio of engine (发动机节流比)
    tr = 1

    # proportion of the thrust between the current situation and the static one at sea level
    alpha = 0

    if theta0 <= tr:
        alpha = delta0*(1-0.49*math.sqrt(Ma))
    else:
        alpha = delta0*(1-0.49*math.sqrt(Ma)-3*(theta0-tr)/(1.5+Ma))

    real_thrust = alpha * thrust_sea_level

    return real_thrust


def SFC(Ma=0, h=0):

    result_sfc = c*(1-0.15*ratio_bypass**0.65) * \
        (1+0.28*(1+0.063*ratio_bypass**1)*Ma) * \
        atmo.density_proportion(h)**0.08

    return result_sfc


# define the list of Ma
Ma = []
for i in range(0, 10):
    tem = i/10
    Ma.append(tem)
Ma.insert(9, 0.85)
print(Ma)

# define the list of altitude
alt = []
for i in range(0, 16000, 2000):
    alt.append(i)

# define and compute the thrust
thr = []
for j in range(0, 8):
    tem = []
    for i in range(0, 11):
        tem.append(thrust(Ma[i], alt[j]))
    thr.append(tem)

print(thr)

# plot the diagram
for i in range(0, 8):
    plt.plot(Ma, thr[i], marker='d',label='Altitude = {}'.format(alt[i]))
    plt.xlim(-0.1,1)
    # plotting the signs (or legends)
    plt.legend()

plt.grid()
plt.xlabel('Ma')
plt.ylabel('Thrust(kg)')
plt.show()

# define and compute the SFC
sfc = []

# define the correction coefficient

coe_correction=sfc_initial/(SFC(Ma[0],alt[0])/10**6*3600)


for j in range(0, 8):
    tem = []
    for i in range(0, 11):
        tem.append(SFC(Ma[i], alt[j])*coe_correction/10**6*3600)
    sfc.append(tem)

print(sfc[0][0])

# plot the diagram
for i in range(0, 8):
    plt.plot(Ma, sfc[i],marker='o',label='Altitude = {}'.format(alt[i]))
    plt.xlim(-0.1,1)
    # plotting the signs (or legends)
    plt.legend()

plt.grid()
plt.xlabel('Ma')
plt.ylabel('SFC(kg/N/h)')
plt.show()
