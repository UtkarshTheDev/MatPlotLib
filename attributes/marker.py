import matplotlib.pyplot as plt
from data.list import n

plt.plot(n, marker="o", markerfacecolor="blue", markersize=7, ls="--", linewidth=3)
# Marker Types
plt.plot(n, marker="o")
plt.plot(n, marker="d")
plt.plot(n, marker="s")
plt.plot(n, marker="p")
plt.plot(n, marker="h")
plt.plot(n, marker="H")
plt.plot(n, marker="D")
plt.plot(n, marker="^")
plt.plot(n, marker="v")
plt.plot(n, marker="<")
plt.plot(n, marker=">")
plt.plot(n, marker="1")
plt.plot(n, marker="2")
plt.plot(n, marker="3")
plt.plot(n, marker="4")

# Marker Size
plt.plot(n, marker="o", markersize=7, ls="--", linewidth=3)

# Marker Color
plt.plot(n, marker="o", markeredgecolor="blue")

# Marker Edge Width
plt.plot(n, marker="o", markeredgewidth=5)

# Marker Face Color
plt.plot(n, marker="o", markerfacecolor="blue")

# All in One
plt.plot(n, marker="o", markerfacecolor="blue", markeredgecolor="blue", markeredgewidth=5, markersize=7, ls="--", linewidth=3)

plt.show()
