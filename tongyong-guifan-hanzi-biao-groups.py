import json

chars_per_syllable = {}

file_input = open('tongyong-guifan-hanzi-biao.txt', 'r')
file_output = open('tongyong-guifan-hanzi-biao-groups.txt', 'w')

for line in file_input:
  _, character, syllables = line.split('	')
  character = character.rstrip()
  syllables = syllables.split(',')
  for syllable in syllables:
    syllable = syllable.strip()
    if syllable in chars_per_syllable:
      chars_per_syllable[syllable].append(character)
    else:
      chars_per_syllable[syllable] = [character]

file_output.write(json.dumps(chars_per_syllable, indent=2, ensure_ascii=False))
