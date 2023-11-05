# Plots the director field
import numpy as np
import matplotlib.pyplot as plt
import math

k1,x1,y1 = 1,2,0
k2,x2,y2 = 1,-2,0
xplus = np.arange(0.2, 5, 0.5)
xb = np.concatenate((-np.flip(xplus), xplus), axis=None)
yb = np.concatenate((-np.flip(xplus), xplus), axis=None)
""" xa = np.concatenate((-np.linspace(0.1,5+1/7,10),np.linspace(0.1,5+1/7,10)), axis=None)
ya = np.concatenate((-np.linspace(0.1,5+1/7,10),np.linspace(0.1,5+1/7,10)), axis=None) """
x,y = np.meshgrid(xb, yb)
fig, ax = plt.subplots()

phi_1 = k1*np.arctan((y-y1)/(x-x1))
phi_2 = k2*np.arctan((y-y2)/(x-x2))
phi = phi_1 + phi_2
phi_01 = 0
phi_02 = 0
phi_0 = phi_01 + phi_02
n_x, n_y = np.cos(phi + phi_0), np.sin(phi + phi_0)

""" # morda to bolj prav. če ne imata oba defekta isto lastno orientacijo
n_x1, n_y1 = np.cos(phi + phi_01), np.cos(phi + phi_01)
n_x2, n_y2 = np.cos(phi + phi_02), np.cos(phi + phi_02)
n_x = n_x1 + n_x2
ny = n_y1 + n_y2
 """
plt.quiver(x,y,n_x,n_y, headlength=0, headaxislength=0)
velikost = 90
plt.scatter(x1, y1, s=velikost, c='blue')
plt.scatter(x2, y2, s=velikost, c='blue')
ax.set_axis_off()
plt.text(x1+0.5, y1-0.5, f"k = {k1}", fontsize=10, c='red', bbox={'facecolor': 'white', 'alpha': 1})
plt.text(x2+0.5, y2-0.5, f"k = {k2}", fontsize=10, c='red', bbox={'facecolor': 'white', 'alpha': 1})
plt.savefig("figures/orient_dva_" + f"{k1}{k2}" + ".png", dpi=1000)
plt.show()