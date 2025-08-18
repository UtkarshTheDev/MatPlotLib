import matplotlib.pyplot as plt
import math

n = [1,2,3,4,5]
m = [2,4,6,8,10]

# Line
plt.plot(n,m)

# Attributes
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Graph")

# Color
plt.plot(n,m, color="red")

plt.show()