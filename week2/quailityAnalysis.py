import numpy as np
import matplotlib.pyplot as plt

# ====== STEP 1: ADD YOUR RATINGS ======
APP1_RATINGS = [4, 4, 4, 4.6, 4, 4, 3.8, 4.2]
APP2_RATINGS = [3.2, 3.5, 4, 3, 3, 2.8, 5, 3.6]

# ====== STEP 2: DEFINE WEIGHTS (same as Excel) ======
# Make sure these match your Excel sheet exactly
WEIGHTS = [0.1, 0.1, 0.15, 0.15, 0.1, 0.1, 0.15, 0.15]

# ====== STEP 3: CALCULATE WEIGHTED SCORES ======
def weighted_score(ratings, weights):
    return sum(r * w for r, w in zip(ratings, weights))

app1_score = weighted_score(APP1_RATINGS, WEIGHTS)
app2_score = weighted_score(APP2_RATINGS, WEIGHTS)

# ====== STEP 4: PRINT OUTPUT ======
print("=== QUALITY ANALYSIS ===")
print(f"App 1 Weighted Score: {app1_score:.2f}")
print(f"App 2 Weighted Score: {app2_score:.2f}")

# ====== STEP 5: RADAR CHART ======
labels = [
    "Feature1", "Feature2", "Feature3", "Feature4",
    "Feature5", "Feature6", "Feature7", "Feature8"
]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

# close the loop
APP1 = APP1_RATINGS + [APP1_RATINGS[0]]
APP2 = APP2_RATINGS + [APP2_RATINGS[0]]
angles += angles[:1]

# plot
fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

ax.plot(angles, APP1, label='WhatsApp')
ax.fill(angles, APP1, alpha=0.1)

ax.plot(angles, APP2, label='Telegram')
ax.fill(angles, APP2, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

ax.set_title("App Quality Comparison Radar Chart")
ax.legend(loc='upper right')

# ====== STEP 6: SAVE FILE ======
plt.savefig("quality_radar_chart.png")
print("Radar chart saved as quality_radar_chart.png")

plt.show()