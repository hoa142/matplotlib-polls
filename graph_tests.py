import matplotlib.pyplot as plt

plt.figure()
# lines = plt.plot([1, 2, 3, 4], [3, 5, 9, 25])
# plt.setp(lines, color="#ff5566")

plt.xlabel("Categories")
plt.ylabel("Amounts")
plt.title("Categories vs. Amounts")

lines = plt.plot(["Men", "Women", "Children"], [3, 5, 9])
plt.show()
