# Plots the plane cut
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

fig, ax = plt.subplots()

# cuts
x1, y1 = [1, 8], [0.1, 0.1]
x2, y2 = [1, 8], [-0.1, -0.1]
plt.plot(x1, y1, x2, y2, c='black')


# tocke, zato da pride lepo v sliko noter
xs = np.array([-6, 16.6])
ys = np.array([0, 0])
plt.scatter(xs, ys)



# arrows
start_point = (0, 0)
end_point = (4, 4)

# Plot the arrow
x_a1 = 7.5
x_a2 = 7.5
y_a1 = 1.1
y_a2 = -1.1
dx_a1 = -0.7
dx_a2 = -0.7
dy_a1 = -0.7
dy_a2 = 0.7
x_a3 = 3
y_a3 = 0.15
dx_a3 = 0
dy_a3 = 1

plt.arrow(x_a1, y_a1, dx_a1, dy_a1, length_includes_head=True, head_length=0.2, head_width=0.3)
plt.arrow(x_a2, y_a2, dx_a2, dy_a2,length_includes_head=True, head_length=0.2, head_width=0.3)
plt.arrow(x_a3, y_a3, dx_a3, dy_a3, length_includes_head=True, head_length=0.2, head_width=0.3)



# defekt
plt.scatter(0, 0, c='black', s=10)



# krog
# Define the center and radius of the circle
center = (0, 0)
radius = 1

# Define the start and end angles (in radians) to create a partial circle
start_angle = np.pi *0.05  # Start angle in radians
end_angle = np.pi *1.95  # End angle in radians

# Create an array of angles between start and end angles
angles = np.linspace(start_angle, end_angle, 100)

# Calculate the x and y coordinates of the points on the circle
x = center[0] + radius * np.cos(angles)
y = center[1] + radius * np.sin(angles)

# Plot the partial circle contour
plt.plot(x, y, c='black')



center_k = (0, 0)
radius_k = 1.7

start_angle_k = np.pi *0.15  # Start angle in radians
end_angle_k = np.pi *0.6
angles_k = np.linspace(start_angle_k, end_angle_k, 100)

x = center_k[0] + radius_k * np.cos(angles_k)
y = center_k[1] + radius_k * np.sin(angles_k)

plt.plot(x, y, c='black')


plt.arrow(x[-1], y[-1], -0.2, -0.08, length_includes_head=True, head_length=0.2, head_width=0.3)


# text
plt.text(x_a1+0.5, y_a1+0.5, r"$\Sigma^{-}$, $\phi = 0$", fontsize=13, c='black')
plt.text(x_a2+0.5, y_a2-0.5, r"$\Sigma^{+}$, $\phi = 2k\pi$", fontsize=13, c='black')
plt.text(x_a3+0.4, y_a3+dy_a3, r"$\mathbf{\hat{e}}_{\varphi}$", fontsize=13, c='black') # \mathbf pride od tukaj: https://stackoverflow.com/questions/14324477/bold-font-weight-for-latex-axes-label-in-matplotlib

    


# Set axis limits for a square aspect ratio (optional)
plt.axis('equal')

ax = plt.gca()
ax.set_xlim([-3, 13])
#plt.axis('off')

plt.savefig('figures/rez2.png', dpi=1000) # default dpi je 100
# Show the plot
plt.show()








