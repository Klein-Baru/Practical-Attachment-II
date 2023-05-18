import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Olympic 100m men's dataset_edited.csv")
df.astype(float)

y = []
for i in df["x"]:

    result = 36.416 - (0.013 * i)
    y.append(result)

print("X-values below, 2nd column\n", df["x"])
print("\n\nY-values: ", y)

plt.xlabel("Year.")
plt.ylabel("Time(seconds)")
plt.title("Olympic 100 metres Men.")

plt.scatter(df["x"], y)  # scatter plot diagram.

plt.plot(df["x"], y)  # line of best fit

plt.show()

print("The equation is thus verified; the graph generated is almost similar Fig 1.5!!!")
