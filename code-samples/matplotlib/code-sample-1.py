import numpy as np
import matplotlib.pyplot as plt

# Create data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot a line chart
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')
plt.show()