import matplotlib.pyplot as plt
import numpy as np

# Create a scatter plot with color mapping
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = np.random.rand(100) * 100
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Color Mapping')
plt.colorbar()
plt.show()