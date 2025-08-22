import matplotlib.pyplot as plt
from data.dataframe import df

plt.xlabel("ODI")
plt.ylabel("Test")
plt.title("ODI vs Test")


plt.plot(df.ODI,color="red", marker="o", markerfacecolor="blue", markersize=7, ls="--", linewidth=3)
plt.plot(df.Test, color="blue", marker="d", markerfacecolor="green", markersize=7, ls="-", linewidth=3)
plt.legend(loc="upper right")
plt.show()