import numpy as np
import matplotlib.pyplot as plt

# Create data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot a scatter plot
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()