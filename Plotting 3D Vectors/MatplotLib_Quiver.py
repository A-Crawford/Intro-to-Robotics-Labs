import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Define a vector [1, 5, 10] # Recall vector has magnitude and direction in a cartesian coordinate system
vector = np.array([1,5,10])
# Define the origin of the vector as [0, 0, 0]
origin = np.array([0, 0, 0])
# Now we can create a 3D plot for the vector
figure = plt.figure() # Create a figure object for the 3D plot
ax = figure.add_subplot(111, projection='3d')
# Plot the vector in 3D space
ax.quiver(origin, origin, origin, vector[0], vector[1], vector[2], color='b') # 

# Set the limits for the plot based on vector's elements
ax_lower_limit=-5 # We can control the lower limit of the axis
ax_upper_limit=5
ax.set_xlim([ax_lower_limit, vector[0]+ax_upper_limit]) #We can now control the X - axis limits
ax.set_ylim([ax_lower_limit, vector[1]+ax_upper_limit])
ax.set_zlim([ax_lower_limit, vector[2]+ax_upper_limit])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.figure.show()

input('hold)')
