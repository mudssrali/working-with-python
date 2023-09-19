import matplotlib.pyplot as plt
import numpy as np

# Create data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple lines on the same chart
plt.plot(x, y1, label='Sine')
plt.plot(x, y2, label='Cosine')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.show()