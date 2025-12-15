
filename = input("Enter file name (with path): ")
keyword = input("Enter keyword to search: ").lower()

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read().lower()

keyword_len = 0
for _ in keyword:          
    keyword_len += 1

text_len = 0
for _ in text:
    text_len += 1

positions = []
i = 0

while i <= text_len - keyword_len:
    j = 0
    match = True
    while j < keyword_len:
        if text[i + j] != keyword[j]:
            match = False
            break
        j += 1
    if match:
        positions.append(i)
    i += 1

if positions:
    print(f"\nKeyword '{keyword}' found {len(positions)} times at positions: {positions}")
else:
    print(f"\nKeyword '{keyword}' not found in the document.")

