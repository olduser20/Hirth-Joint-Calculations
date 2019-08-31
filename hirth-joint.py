

import numpy as np





##### Gear geometry #####
# Inner radius
Ri=17.0           # [mm]
d=2*Ri
# Outer radius
Ro=24.75           # [mm]
D=2*Ro
# Mean radius
Rm=(Ri+Ro)/2        # [mm]

# Number of teeth
z=24

# Smallest tooth height
hp=2.78         # [mm]
# Biggest tooth height
hpp=4.59          # [mm]
# G Point (Center of Gravity)
hG= (hp+hpp)/2/2        # [mm]

# Smallest tooth thickness
ap=3.92         # [mm]
# Biggest tooth thickness
app=5.95       # [mm]

# Tooth length
L=Ro-Ri         # [mm]

# Fixing hole diameter
dL=0            # [mm]
# Number of fixing holes
nb=0

# Tooth root radius
r=0.3           # [mm]

# Crown clearance
s=0.43           # [mm]

# Load bearing percentage (0.65 for milled; 0.75 for grinded teeth)
eta_z=0.75

# Effective tooth flank area
Az=(D-d-nb*np.power(dL,2)/(D+d))*(np.pi/4*(D+d)-1.155*z*(r+s))*eta_z
print("Az = " + str(Az))

##### Load calculations #####
# External torque to be transmitted
T= 100e3          # [N-mm]

# Total tangential force
Fu=np.round(T/Rm,1)         # [N]
print("Fu = " + str(Fu))


# Axial force (friction neglected)
Fa=np.round(Fu*np.tan(np.pi/3),1)

print("Fa = " + str(Fa))


##### Stress calculations #####
# Bending stress
sigma_b=np.round(6*Fu*hG/(L*np.power((ap+app)/2,2)),1)      # [MPa]

print("sigma_b = " + str(sigma_b))

# Shear stress
tau= np.round(16*T/(np.pi * np.power(2*Ro,3)*(1-np.power(Ri/Ro,4))),1)   # [MPa]
print("Tau = " + str(tau))


##### Calculating Preload #####
# Preload safety factor (between 1.8 to 3)
SF=2.5

# Prelaod
Fva=Fa*SF           # [N]
print("Preload = " + str(Fva))

# Maximum pressure on tooth flank
p_max=np.round((Fva+Fa)/Az,1)
print("p_max = " + str(p_max))


# Factor c for 24 teeth
c=0.114     

# h estimation
h=c*D-(2*r+s)
print("h = " + str(h))




