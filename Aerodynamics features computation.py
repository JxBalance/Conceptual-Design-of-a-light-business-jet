# computation preperation
import math

# ploting preperation
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class DesignFactors:

    # difine the area of the refering wing
    area_wing = 25.83

    # difine the wing span
    b_wingspan = 15

    # difine the sweep angle of the front line of the wing
    sweepangle_fro = 27/360*math.pi

    # difine the sweeep angle of the maximum thickness line
    sweepangle_maxthl = 22/360*math.pi

    # define the length of MAC
    length_mac = 2.01

    # define the area of the horizontal tail
    area_htail = 6.56

    # difine the sweeep angle of the horizontal tail maximum thickness line
    sweepangle_htailmaxthl = 20/360*math.pi

    # define the Aspect Ratio of wing
    aspectratio_wing = 9

    # define the Aspect Ratio of horizontal tail
    aspectratio_htail = 4

    # define the taper ratio
    lambda_ratio_taper = 0.19

    # define the geometric average chord length of the horizontal tail
    chord_avrhtail = (0.66+1.645)/2

    # define the vertial distance between the wing and the horizontal tail
    z_ht = 3.719

    # difine the horizontal distance between the 1/4 point of the wing and the 1/4 point of the ht
    l_ht = 5.717

    # define the zero lift angle of airfoil in degree
    angle_zerolift_airfoil = -3.7

    # define the installation angle
    angle_installation = -1.0

    # define the dihedral angle
    angle_dihedral = 2/180*math.pi

    # define the relative thickness of airfoil
    thickness_airfoil = 0.12

    # define the projected area of the fuselage from sides
    area_fuselage_side = 31.3248

    # defiene the projected area of the fuselage frome above
    area_fuselage_above = 29.2423


class Fuselagefeatures:

    # instantiation of the factors
    def __init__(self):
        self.factors2 = DesignFactors()

    # caculate the wet area of the wing through the function

    def wing_wetarea(self):

        # simplify the factors
        s = self.factors2.area_wing

        # define the exposed area of wing
        area_exwing = s/math.cos(self.factors2.angle_dihedral)

        # define the wet area of the wing
        if self.factors2.thickness_airfoil < .05:
            area_wet_wing = 2.003*area_exwing
        else:
            area_wet_wing = area_exwing * \
                (1.977+0.52*self.factors2.thickness_airfoil)

        return area_wet_wing

    # caculate the wet area of the fuselage through the function
    def fuselage_wetarea(self):
        'The default intersecting surface is regarded as the normal'
        'Thus the coefficient of the wet area caculation is taken as 3.4'

        # simply the factors
        a_side = self.factors2.area_fuselage_side
        a_above = self.factors2.area_fuselage_above

        # for the fuselage with the general intersecting surface
        # the caculation coefficient could be taken as 3.4
        k = 3.4

        s_wet = k*(a_above+a_side)/2

        return s_wet

    def wetarea_whole(self):
        s_wet_whole = self.fuselage_wetarea()+self.wing_wetarea()
        return s_wet_whole


class LiftingLineSlope:

    # instantiation of the factors
    def __init__(self):
        self.factors = DesignFactors()

    # caculate the clalpha in low speed first

    def clalphainlowspeed(self):

        # simplify the factors
        s = self.factors.area_wing
        s_ht = self.factors.area_htail

        p = math.pi
        A = self.factors.aspectratio_wing
        A_ht = self.factors.aspectratio_htail

        # Define the lifting line slope of airfoil
        # caculated by analyzed the lifting line's slope in profili
        clalpha_airfoil = 1.5/(9.1-(-1)*3.7)

        # caculate the Correction coefficient of non-elliptic wing
        e = 2 / \
            (2-A +
             math.sqrt(4 + A**2 *
                       (1+(math.tan(self.factors.sweepangle_maxthl))**2)))

        # caculate the lifting line slope of the wing
        clalpha_wing = clalpha_airfoil /\
            (1+(57.3*clalpha_airfoil/(p*e*A)))

        # caculate the clalpha of the horizontal tail
        e_ht = 2 / \
            (2-A_ht+math.sqrt(4 + A_ht ** 2 *
                              (1+(math.tan(self.factors.sweepangle_htailmaxthl))**2)))

        # caculate the lifting line slope of the horizontal tail
        clalpha_htail = clalpha_airfoil / \
            (1+(clalpha_airfoil/(p*e_ht*A_ht)))

        # now consider the effect of the down wash brought by the wing
        # caculate the coefficient of the wing down wash first
        coe_wingandtail = 21*clalpha_airfoil/A**0.725 * \
            (self.factors.chord_avrhtail/self.factors.l_ht) * \
            ((10-3*self.factors.lambda_ratio_taper)/7) * \
            (1 - self.factors.z_ht/self.factors.b_wingspan)

        # caculate the contribution for the claplha of the tail
        delta_clalpha_htail = clalpha_htail*(1-coe_wingandtail)*s_ht/s

        # sum and get the clalpha of entire plane
        clalpha_total = clalpha_wing+delta_clalpha_htail

        return clalpha_total

    # Define the method to caculate the clalpha of the whole aircraft

    def clalphacomputation(self, Ma):

        # low speed situation
        if Ma <= 0.3:

            # determine the clalpha in low speed
            clalpha_total_result = self.clalphainlowspeed()

        elif 0.3 < Ma < 0.99:

            # get the clalpha in low speed first
            cla_inlowspeed = self.clalphainlowspeed()

            # convert into the clalpha in subsonic
            clalpha_total_result = cla_inlowspeed/math.sqrt(1-Ma**2)

        else:
            raise NotImplementedError("out of the capability of this part")

        return clalpha_total_result


###
# the following part is about the lift coefficient of the airplane
###

# instantiation of the computation
cla = LiftingLineSlope()

# difine the factor lists of Ma
Ma = []
for i in range(0, 10, 1):
    tem_i = i/10
    Ma.append(tem_i)

# import Ma = 0.85
Ma.insert(9, 0.85)

# difine the factor lists of angle of attack
angle_attack = []
for i in range(-5, 10, 1):
    angle_attack.append(i)


# define the cl computation function
def clcomputation(Ma, alpha):
    features = DesignFactors()
    slope = cla.clalphacomputation(Ma)
    cl = slope*(alpha+features.angle_installation -
                features.angle_zerolift_airfoil)
    return cl


# define the cl, a 9X14 list
cl = []

# caculate the cl and generalize the results
for j in Ma:
    tem = []
    for i in angle_attack:
        tem.append(clcomputation(j, i))
    cl.append(tem)


for i in range(0, 11, 1):
    temma = Ma[i]
    plt.plot(angle_attack, cl[i], marker='o', label='Ma = {}'.format(temma))

    # plotting the signs (or legends)
    plt.legend()

plt.grid()
plt.xlabel('Angle of attack')
plt.ylabel('CL')
plt.show()

###
# the following part is about the drag coefficient of the airplane
###


# get the wet area of the fuselage
fusf = Fuselagefeatures()
area_wet_whole = fusf.wetarea_whole()

# define the equivalent skin friction resistance coefficient
# for civil airplane
cfe = 0.003

# caculate the drag in zero lift of the entire airplane
cd0 = cfe*area_wet_whole/cla.factors.area_wing

# caculate the backsweep-induced factor within lift-induced drag coefficient
e_drag_lift = 4.61*(1-0.045*cla.factors.aspectratio_wing**0.68) * \
    (math.cos(cla.factors.sweepangle_fro))**0.15-3.1


# caculate the lift-induced drag coefficient
k_drag_lift = 1/math.pi/cla.factors.aspectratio_wing/e_drag_lift

# define the drag factors
cd = []

# caculate the drag features of the whole airplane
# j stands for Ma
# i stands for angle
for j in range(0, 11, 1):
    tem = []
    for i in range(0, 15, 1):

        temresult = cd0+k_drag_lift*cl[j][i]**2

        tem.append(temresult)

    cd.append(tem)

for i in range(0, 11, 1):
    temma = Ma[i]
    plt.plot(angle_attack, cd[i], label='Ma = {}'.format(temma))

    # plotting the signs (or legends)
    plt.legend()

plt.grid()
plt.xlabel('Angle of attack')
plt.ylabel('CD')
plt.show()


###
# the following part is about the L/D ratio
###

# define the LD ratio
ratio_LD = []

# caculate the LD ratio
for j in range(0, 11, 1):
    tem = []
    for i in range(0, 15, 1):

        temresult = cl[j][i]/cd[j][i]

        tem.append(temresult)

    ratio_LD.append(tem)

for i in range(0, 11, 1):
    temma = Ma[i]
    plt.plot(angle_attack, ratio_LD[i], marker='d', label='Ma = {}'.format(temma))

    # plotting the signs (or legends)
    plt.legend()

plt.grid()
plt.xlabel('Angle of attack')
plt.ylabel('LD Ratio')
plt.show()
