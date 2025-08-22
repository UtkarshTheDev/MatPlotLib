import matplotlib.pyplot as plt
from data.list import n,m
from data.dataframe import df

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

# With Legend
plt.plot(n,label="List of n")
plt.plot(m,label="List of m")
plt.legend(loc="upper right")

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