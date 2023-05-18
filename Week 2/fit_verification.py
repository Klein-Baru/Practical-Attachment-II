import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Olympic 100m men's dataset.xlsx")
df.astype(float)

plt.scatter(df["x"], df["y"])

y = []
for i in df["x"]:

    result = 36.416 - (0.013 * i)
    y.append(result)

print("X-values below, 2nd column\n\r", df["x"])
print("\n\nY-values: ", y)

plt.xlabel("Year.")
plt.ylabel("Time(seconds).")
plt.title("Olympic 100 metres Men.")

plt.plot(df["x"], y)  # line of best fit

plt.show()

while True:
    print("The equation is wrong!!")