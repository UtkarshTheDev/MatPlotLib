import matplotlib.pyplot as plt
from data.list import n,m
from data.dataframe.data import df

# Line
# plt.plot(n,m)

# Attributes
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Graph")


# Color
plt.plot(n, color="red")
plt.plot(m, color="blue")

# Line Width
plt.plot(n,linewidth=5)
plt.plot(m,linewidth=5)

# With Legend
plt.plot(n,label="List of n")
plt.plot(m,label="List of m")
plt.legend(loc="upper right")

# Line Style
plt.plot(n,ls="--")
plt.plot(m,ls="-")

# Marker
plt.plot(n,marker="o")
plt.plot(m,marker="d")

# Marker Size
plt.plot(n,marker="o",markersize=10)
plt.plot(m,marker="d",markersize=10)

# Marker Color
plt.plot(n,marker="o",markerfacecolor="red")
plt.plot(m,marker="d",markerfacecolor="green")

# Marker Edge Color
plt.plot(n,marker="o",markeredgecolor="blue")
plt.plot(m,marker="d",markeredgecolor="yellow")

# Marker Edge Width
plt.plot(n,marker="o",markeredgewidth=5)
plt.plot(m,marker="d",markeredgewidth=5)

# Marker Size
plt.plot(n,marker="o",markersize=10)
plt.plot(m,marker="d",markersize=10)

# All in One
plt.plot(n,marker="o",markerfacecolor="red",markeredgecolor="blue",markeredgewidth=5,markersize=10,linewidth=5,ls="--",color="red",label="List of n")
plt.plot(m,marker="d",markerfacecolor="green",markeredgecolor="yellow",markeredgewidth=5,markersize=10,linewidth=5,ls="--",color="green",label="List of m")
plt.legend(loc="upper right")
plt.show()