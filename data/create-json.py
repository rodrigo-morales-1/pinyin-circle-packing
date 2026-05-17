import json
import os
import unicodedata

# Code retrieved from https://stackoverflow.com/a/518232
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def has_only_ascii(s):
   for c in (s):
      # 97 = a, 122 = z
      # 65 = A, 90 = Z
      if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90:
         return True
   raise Exception(f"Syllable {s} contain characters that are not ASCII")

def child_with_id(parent, id):
    for child in parent['children']:
        if child['id'] == id:
            return child
    return False

data_output = [
    {
        "id": "root",
        "datum": 1,
        "children": []
    }
]
root = data_output[0]

file_input = open('tongyong-guifan-hanzi-biao.txt', 'r')

for line in file_input:
    _, character, syllables = line.split('	')
    character = character.rstrip()
    syllables = syllables.split(',')
    for syllable in syllables:
        syllable_with_accents = syllable.strip()
        syllable_no_accents = strip_accents(syllable_with_accents)
        has_only_ascii(syllable_no_accents)
        child_root_depth_1 = child_with_id(root, syllable_no_accents)
        if not child_root_depth_1:
            root['children'].append({
                "id": syllable_no_accents,
                "children": [
                    {
                        'id': syllable_with_accents,
                        'children': [
                            {
                                'id': character,
                                'datum': 1
                            }
                        ]
                    }
                ]
            })
        else:
            child_root_depth_2 = child_with_id(child_root_depth_1, syllable_with_accents)
            if not child_root_depth_2:
                child_root_depth_1['children'].append({
                    "id": syllable_with_accents,
                    "children": [
                        {
                            'id': character,
                            'datum': 1
                        }
                    ]
                })
            else:
                child_root_depth_2['children'].append({
                    'id': character,
                    'datum': 1
                })

# Set datum
root = data_output[0]
for children_root_depth_1 in root['children']:
    children_root_depth_1_datum = 0
    for children_root_depth_2 in children_root_depth_1['children']:
        children_root_depth_2_count_chinese_characters = len(children_root_depth_2['children'])
        children_root_depth_2['datum'] = children_root_depth_2_count_chinese_characters
        children_root_depth_1_datum += children_root_depth_2_count_chinese_characters
    children_root_depth_1['datum'] = children_root_depth_1_datum

file_output = open(os.path.basename(__file__) + '.json', 'w')
file_output.write(json.dumps(data_output, indent=4, ensure_ascii=False))
