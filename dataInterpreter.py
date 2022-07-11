import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filteredStarsChart.csv")
df.head()

star_name = df["Name"].to_list()
star_mass = df["Mass"].to_list()
star_radius = df["Radius"].to_list()
star_distance = df["Distance"].to_list()
star_gravity = df["Gravity"].to_list()

plt.barh(star_name, star_mass)
plt.ylabel("Star Name")
plt.xlabel("Star Mass")
plt.title("Names vs. Mass of Stars")
plt.show()

plt.barh(star_name, star_radius)
plt.ylabel("Star Name")
plt.xlabel("Star Radius")
plt.title("Names vs. Radii of Stars")
plt.show()

plt.barh(star_name, star_distance)
plt.ylabel("Star Name")
plt.xlabel("Star Distance (from Earth)")
plt.title("Names vs. Distance (from Earth) of Stars")
plt.show()

plt.barh(star_name, star_gravity)
plt.ylabel("Star Name")
plt.xlabel("Star Gravity")
plt.title("Names vs. Gravity of Stars")
plt.show()
