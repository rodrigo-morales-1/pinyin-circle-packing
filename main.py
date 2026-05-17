import circlify
import matplotlib.pyplot as plt
import os
import json
import time
import datetime

start_time = time.time()

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
figsize = 50
fig, ax = plt.subplots(figsize=(figsize, figsize))

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

circles_line_width=0.5
pinyin_boxes_line_width=0.5

for circle in circles:
    # Circles in depth level 1
    if circle.level == 1:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black", linewidth=circles_line_width))
    # Circles in depth level 2: Pinyin without accents
    if circle.level == 2:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black", linewidth=circles_line_width))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y + r), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         linewidth=pinyin_boxes_line_width,
                         pad=.25))
    # Circles in depth level 3: Pinyin with accents
    if circle.level == 3:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black", linewidth=circles_line_width))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y + r), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         linewidth=pinyin_boxes_line_width,
                         pad=.25))
    # Circles in depth level 4: Chinese characters
    elif circle.level == 4:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="lightblue"))
        # Show label
        label = circle.ex["id"]
        plt.annotate(label, (x, y), va='center', ha='center', color="black")


# Save PNG image
os.chdir(os.path.dirname(__file__))
dpi = 300
output_file = f'python-pinyin-dpi-{dpi}-figsize-{figsize}-' + time.strftime("%Y-%m-%dT%H-%M-%S") + '.png'
plt.savefig(output_file, dpi=dpi)

# Print execution time
elapsed_seconds = time.time() - start_time
elapsed_time = datetime.timedelta(seconds=elapsed_seconds)
print(f"--- Execution time: {elapsed_time} ---")


