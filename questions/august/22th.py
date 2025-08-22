import pandas as pd
import matplotlib.pyplot as plt

# Ques 1: Mela Sales Report
# Given Data:

data = {
    "Week1": [500,5900,6500,3500,4000,5300,7900],
    "Week2": [4000,3000,5000,5500,3000,4300,5900],
    "Week3": [4000,4800,3500,2500,3000,5300,6000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Solution:

plt.plot(df.Week1, color="Red", marker="o", markerfacecolor="blue", markersize=7, ls="--", linewidth=3)
plt.plot(df.Week2, color="Blue", marker="d", markerfacecolor="green", markersize=7, ls="-", linewidth=3)
plt.plot(df.Week3, color="Brown", marker="s", markerfacecolor="yellow", markersize=7, ls="-.", linewidth=3)

# (i) Title
plt.title("Mela Sales Report")
# (ii) X Label
plt.xlabel("Days")
# (iii) Y Label
plt.ylabel("Sales in Rs.")

# (iv) Legend
plt.legend(loc="upper right")

plt.show()