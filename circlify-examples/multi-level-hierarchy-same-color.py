# import libraries
import circlify
import matplotlib.pyplot as plt
import os

data = [
    {
        "id": "root",
        "datum": 6964195249,
        "children": [
            {
                "id": "c1",
                "datum": 450448697,
                "children": [
                    {
                        "id": "c1-c1",
                        "datum": 1,
                    },
                    {
                        "id": "c1-c2",
                        "datum": 1
                    },
                    {
                        "id": "c1-c3",
                        "datum": 1
                    }
                ]
            },
            {
                "id": "c2",
                "datum": 278095425,
                "children": [
                    {
                        "id": "c2-c1",
                        "datum": 1
                    },
                    {
                        "id": "c2-c2",
                        "datum": 1
                    },
                    {
                        "id": "c2-c3",
                        "datum": 1
                    }
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
    # Circles in depth level 2
    if circle.level == 2:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.5,
                                linewidth=2, color="lightblue"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y), va='center', ha='center', bbox=dict(
            facecolor='white', edgecolor='black', boxstyle='round', pad=.5))
    # Circles in depth level 3
    elif circle.level == 3:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0))
        label = circle.ex["id"]
        plt.annotate(label, (x, y), ha='center', color="black")
    # Circles in depth level 4
    elif circle.level == 4:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.6, linewidth=1, color="#ff9f43"))
    # Circles in depth level 5
    elif circle.level == 5:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.8, linewidth=1, color="#ee5253"))

for circle in circles:
    if circle.level > 2:
        x, y, r = circle

plt.savefig(os.path.basename(__file__) + '.png')
