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

file_input = open('tongyong-guifan-hanzi-biao.txt', 'r')
file_output = open(os.path.basename(__file__) + '.txt', 'w')

for line in file_input:
    _, character, syllables = line.split('	')
    character = character.rstrip()
    syllables = syllables.split(',')
    for syllable in syllables:
        syllable_with_accents = syllable.strip()
        syllable_no_accents = strip_accents(syllable_with_accents)
        has_only_ascii(syllable_no_accents)
        file_output.write(f"{character}	{syllable_with_accents}	{syllable_no_accents}\n")




