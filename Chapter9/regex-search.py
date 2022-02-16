from pathlib import Path
import re
# get user regex
while True:
    print('Enter a valid path:')
    p = Path(input())
    if p.exists() and p.is_dir():
        break

print('Enter a regular expression:')
regex = input()
check = re.compile(regex)
for textFile in list(p.glob('*.txt')):
    with open(textFile) as file:
        results = check.findall(file.read())
        if len(results) > 0:
            print(f'{textFile}:')
            for result in results:
                print(f'Found: {result}')
            print('---')
