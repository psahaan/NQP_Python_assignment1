# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:57:39 2022

@author: Sahaan
"""
import numpy as np
import matplotlib.pyplot as plt

#  Defining  Variables and Constants
chi  = 10 
N = 1e25                                   # Atomic Density 
e = 1.6e-19                                # Electronic charge
m0= 9.1e-31                                # Mass of electron 
w = np.linspace(1e12,150e12,1000)          # Frequency
w0 = 100e12                                # Resonant Frequency
gam = 5e12                                 # gamma 
eps0 = 8.854e-12                           # permittiviy of freespace

#  Formulas for calculating real and imaginary parts of complex permittivity from Mark Fox Textbook 

E1 = 1+chi+(((N*(e**2))/(eps0*m0))*((w0**2-w**2)/((w0**2-w**2)**2+((gam*w)**2))))
E2 = ((N*(e**2))/(eps0*m0))*((gam*w)/((w0**2-w**2)**2+((gam*w)**2)))


# Plotting using Matplotlib 

# Both E1 and E2 in sameplot 

plt.title('Real and Imaginary parts of Complex Permittivity ', fontsize = 12, fontweight = 'bold')
plt.plot(w,E1,label="RealPart", linewidth = 2 )
plt.plot(w,E2,label ="ImaginaryPart",linewidth = 2 )
plt.yticks(np.arange(-30,60,10)) 
plt.grid()
plt.legend([" $\epsilon$1   ","$\epsilon$2  "])
plt.xlabel('Frequency',fontweight = 'bold',fontsize = 11)
plt.ylabel('$\epsilon$  ',fontweight = 'bold',fontsize = 11) 


#  E1 and E2 in different Plots
fig, axs = plt.subplots(1,2)


axs[0].plot(w, E1,linewidth = 2)
axs[0].set_title(' $\epsilon$1  ') 
axs[0].grid()

axs[1].plot(w,E2, 'tab:green',linewidth = 2)
axs[1].set_title(' $\epsilon$2  ') 
axs[1].grid()


fig.suptitle('Real and Imaginary parts of Complex Permittivity ', fontsize = 12, fontweight = 'bold')
for ax in axs.flat:

    ax.set_xlabel('Frequency',fontweight = 'bold',fontsize = 11 )
    ax.set_ylabel('$\epsilon$',fontweight = 'bold',fontsize = 11 )

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()