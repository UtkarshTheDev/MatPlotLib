import matplotlib.pyplot as plt

from data.list import n

plt.hist(n, color="#ff0239", label="n", bins=25)
plt.xlabel("n")
plt.ylabel("Participants")
plt.title("n of Participants")
plt.legend(loc="upper right")
plt.show()
