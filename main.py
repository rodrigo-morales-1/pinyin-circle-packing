# import the circlify library
import circlify
import matplotlib.pyplot as plt

data = [
  {
    "id": "World",
    "datum": 6964195249,
    "children": [
      {
        "id": "North America",
        "datum": 450448697,
        "children": [
          {
            "id": "United States",
            "datum": 308865000
          },
          {
            "id": "Mexico",
            "datum": 107550697
          },
          {
            "id": "Canada",
            "datum": 34033000
          }
        ]
      },
      {
        "id": "South America",
        "datum": 278095425,
        "children": [
          {
            "id": "Brazil",
            "datum": 192612000
          },
          {
            "id": "Colombia",
            "datum": 45349000
          },
          {
            "id": "Argentina",
            "datum": 40134425
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

# Print circle the highest level (continents):
for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5,
                 linewidth=2, color="lightblue"))

# Print circle and labels for the highest level:
for circle in circles:
    if circle.level != 3:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    ax.add_patch(plt.Circle((x, y), r, alpha=0.5,
                 linewidth=2, color="#69b3a2"))
    plt.annotate(label, (x, y), ha='center', color="white")

# Print labels for the continents
for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    label = circle.ex["id"]
    plt.annotate(label,
                 (x, y),
                 va='center',
                 ha='center',
                 bbox=dict(facecolor='white',
                           edgecolor='black',
                           boxstyle='round',
                           pad=.5))

plt.savefig('/tmp/a.png')
