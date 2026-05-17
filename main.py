import circlify
import matplotlib.pyplot as plt
import os
import json

plt.rcParams["font.family"] = "Noto Serif CJK SC"

file_json = 'data/create-json.py.json'
with open(file_json, 'r') as f:
    data = json.load(f)

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(
    data,
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(14, 14))

# Title
ax.set_title('拼音分组汉字图')

# Remove axes
ax.axis('off')

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

for circle in circles:
    # Circles in depth level 1
    if circle.level == 1:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
    # Circles in depth level 2: Pinyin without accents
    if circle.level == 2:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y + r), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         pad=.25))
    # Circles in depth level 3: Pinyin with accents
    if circle.level == 3:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y + r), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         pad=.25))
    # Circles in depth level 4: Chinese characters
    elif circle.level == 4:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="lightblue"))
        # Show label
        label = circle.ex["id"]
        plt.annotate(label, (x, y), va='center', ha='center', color="black")

plt.savefig(os.path.basename(__file__) + '.png', dpi=300)

