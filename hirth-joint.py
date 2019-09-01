

import numpy as np
import matplotlib.pyplot as plt




##### Gear geometry #####
# Inner radius
Ri=17.0           # [mm]
d=2*Ri
# Outer radius
Ro=26           # [mm]
D=2*Ro
# Mean radius
Rm=(Ri+Ro)/2        # [mm]
print("Rm =\t\t" + str(Rm) +"\t\t [mm]")


# Number of teeth
z=24

# Smallest tooth height
hp=2.85         # [mm]
# Biggest tooth height
hpp=4.9          # [mm]
# G Point (Center of Gravity)
hG= (hp+hpp)/2/2        # [mm]
print("hG =\t\t" + str(hG) +"\t\t [mm]")

# Smallest tooth thickness
ap=3.92         # [mm]
# Biggest tooth thickness
app=6.27       # [mm]

# Tooth length
L=Ro-Ri         # [mm]

# Fixing hole diameter
dL=4            # [mm]
# Number of fixing holes
nb=1

# Tooth root radius
r=0.3           # [mm]

# Crown clearance
s=0.4           # [mm]

# Load bearing percentage (0.65 for milled; 0.75 for grinded teeth)
eta_z=0.65

# Effective tooth flank area
Az=np.round((D-d-nb*np.power(dL,2)/(D+d))*(np.pi/4*(D+d)-1.155*z*(r+s))*eta_z,2)
print("Az =\t\t" + str(Az) +"\t\t [mm2]")

##### Load calculations #####
# External torque to be transmitted
T= 141e3          # [N-mm]

# Total tangential force
Fu=np.round(T/Rm,1)         # [N]
print("Fu =\t\t" + str(Fu) +"\t\t [N]")

# Axial force (friction neglected)
Fa=np.round(Fu*np.tan(np.pi/6),1)
print("Fa =\t\t" + str(Fa) +"\t\t [N]")


##### Stress calculations #####
# Bending stress
sigma_b=np.round(6*(Fu/z)*hG/(L*np.power((ap+app)/2,2)),1)      # [MPa]
print("sigma_b =\t" + str(sigma_b) +"\t\t [MPa]")

# Shear stress
tau= np.round(16*T/(np.pi * np.power(2*Ro,3)*(1-np.power(Ri/Ro,4))),1)   # [MPa]
print("Tau =\t\t" + str(tau) +"\t\t [MPa]")

##### Calculating Preload #####
# Preload safety factor (between 1.8 to 3)
SF=2.5

# Prelaod
Fva=Fa*SF           # [N]
print("Preload =\t" + str(Fva) +"\t\t [N]")

# Maximum pressure on tooth flank
p_max=np.round((Fva+Fa)/Az,1)
print("p_max =\t\t" + str(p_max) +"\t\t [MPa]")


# Factor c for 24 teeth
c=0.114     

# h estimation
h=np.round(c*D-(2*r+s),2)
print("h =\t\t" + str(h) +"\t\t [mm]")




