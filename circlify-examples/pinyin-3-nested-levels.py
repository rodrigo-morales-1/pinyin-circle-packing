# import libraries
import circlify
import matplotlib.pyplot as plt
import os

plt.rcParams["font.family"] = "Noto Serif CJK SC"

data = [
    {
        "id": "root",
        "label": "root",
        "datum": 1,
        "children": [
            {
                "id": "c1",
                "label": "yao",
                "datum": 1,
                "children": [
                    {
                        "id": "c1-c1",
                        "label": "yāo",
                        "datum": 1,
                        "children": [
                            {"id": "c1-c1-c1", "label": "夭", "datum": 1},
                            {"id": "c1-c1-c2", "label": "吆", "datum": 1},
                            {"id": "c1-c1-c3", "label": "约", "datum": 1}
                        ]
                    },
                    {
                        "id": "c1-c2",
                        "label": "yáo",
                        "datum": 1,
                        "children": [
                            {"id": "c1-c2-c1", "label": "尧", "datum": 1},
                            {"id": "c1-c2-c2", "label": "侥", "datum": 1},
                            {"id": "c1-c2-c3", "label": "肴", "datum": 1}
                        ]
                    },
                    {
                        "id": "c1-c3",
                        "label": "yǎo",
                        "datum": 1,
                        "children": [
                            {"id": "c1-c3-c1", "label": "咬", "datum": 1},
                            {"id": "c1-c3-c2", "label": "舀", "datum": 1},
                            {"id": "c1-c3-c3", "label": "杳", "datum": 1}
                        ]
                    }
                ]
            },
            {
                "id": "c2",
                "label": "chi",
                "datum": 1,
                "children": [
                    {
                        "id": "c2-c1",
                        "label": "chī",
                        "datum": 1,
                        "children": [
                            {"id": "c2-c1-c1", "label": "吃", "datum": 1},
                            {"id": "c2-c1-c2", "label": "痴", "datum": 1},
                            {"id": "c2-c1-c3", "label": "哧", "datum": 1}
                        ]
                    },
                    {
                        "id": "c2-c2",
                        "label": "chí",
                        "datum": 1,
                        "children": [
                            {"id": "c2-c2-c1", "label": "池", "datum": 1},
                            {"id": "c2-c2-c2", "label": "弛", "datum": 1},
                            {"id": "c2-c2-c3", "label": "驰", "datum": 1}
                        ]
                    },
                    {
                        "id": "c2-c3",
                        "label": "chǐ",
                        "datum": 1,
                        "children": [
                            {"id": "c2-c3-c1", "label": "尺", "datum": 1},
                            {"id": "c2-c3-c2", "label": "齿", "datum": 1},
                            {"id": "c2-c3-c3", "label": "侈", "datum": 1}
                        ]
                    },
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
    # Circles in depth level 2
    if circle.level == 2:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["label"]
        plt.annotate(label, (x, y), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         pad=.5))
    # Circles in depth level 3
    if circle.level == 3:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["label"]
        plt.annotate(label, (x, y), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         pad=.5))
    # Circles in depth level 4
    elif circle.level == 4:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r))
        # Show label
        label = circle.ex["label"]
        plt.annotate(label, (x, y), ha='center', color="black")

plt.savefig(os.path.basename(__file__) + '.png', dpi=100)

