import matplotlib.pyplot as plt
from data.dataframe import df

plt.xlabel("ODI")
plt.ylabel("Test")
plt.title("ODI vs Test")


plt.plot(df.ODI, df.Test)
plt.show()