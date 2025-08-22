import matplotlib.pyplot as plt

# Ques 1:

tenA = [80,30,67,35,90]
tenB = [80,67,32,67,95]

plt.plot(tenA,color="red",label="Ten A",marker="o",markerfacecolor="blue",markersize=10,ls="--",linewidth=5)
plt.plot(tenB,color="blue",label="Ten B",marker="o",markerfacecolor="red",markersize=10,ls="--",linewidth=5)
plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Marks of Ten A and Ten B")
plt.legend(loc="upper right")
plt.show()