import matplotlib.pyplot as plt

# Ques 1: Plot the graph of subjects and highest marks of a participant in each subject
# Given Data:
data = [80,75,70,78,82]
subjects = ["Physics","Chemistry","Maths","Biology","Computer"]

plt.plot(subjects, data, color="black", marker="*", markerfacecolor="black", markersize=7,label="Subjects")
plt.xlabel("Subjects")
plt.ylabel("Highest Marks")
plt.title("Highest Marks of a Participant in Each Subject")
plt.legend(loc="upper right")
plt.show()