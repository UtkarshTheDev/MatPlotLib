import matplotlib.pyplot as plt

# Ques 1:
score=[8,10,15,25,28,35,47,49,50,63,67,53,57,58,69]

plt.hist(score,color="black",label="Score",bins=10)
plt.xlabel("Score")
plt.ylabel("Participants")
plt.title("Score of Participants")
plt.legend(loc="upper right")
plt.show()

# Ques 2: Save it as PDF
plt.savefig("score.pdf")