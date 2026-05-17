import circlify
import matplotlib.pyplot as plt
import os

data = [
    {
        "id": "root",
        "datum": 1,
        "children": [
            {
                "id": "c1",
                "datum": 1,
                "children": [
                    {"id": "c1-c1", "datum": 1},
                    {"id": "c1-c2", "datum": 1},
                    {"id": "c1-c3", "datum": 1}
                ]
            },
            {
                "id": "c2",
                "datum": 1,
                "children": [
                    {"id": "c2-c1", "datum": 1},
                    {"id": "c2-c2", "datum": 1},
                    {"id": "c2-c3", "datum": 1}
                ]
            }
        ]
    }
]

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(
    data,
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(14, 14))

# Title
ax.set_title('The title of my plot')

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
    # Circles in depth level 2
    if circle.level == 2:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y), va='center', ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))
    # Circles in depth level 3
    elif circle.level == 3:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.5, linewidth=2, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y), ha='center', color="black")

plt.savefig(os.path.basename(__file__) + '.png')
