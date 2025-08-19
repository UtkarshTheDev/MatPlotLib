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

# Line Width
plt.plot(n,m,linewidth=5)

# Line Style
plt.plot(n,m,ls="--")

# Marker
plt.plot(n,m,marker="o")

# Marker Size
plt.plot(n,m,markersize=10)

# Marker Color
plt.plot(n,m,marker="o",markerfacecolor="red")

# Marker Edge Color
plt.plot(n,m,marker="o",markeredgecolor="blue")

# Marker Edge Width
plt.plot(n,m,marker="o",markeredgewidth=5)

# Marker Size
plt.plot(n,m,marker="o",markersize=10)

# All in One
plt.plot(n,m,marker="o",markerfacecolor="red",markeredgecolor="blue",markeredgewidth=5,markersize=10,linewidth=5,ls="--",color="red")

plt.show()