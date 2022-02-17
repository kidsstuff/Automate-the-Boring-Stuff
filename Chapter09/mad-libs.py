import re

# Create madlibs file
with open('madlibs.txt', 'w') as file:
    file.write('''The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.''')
    
# Read in the text file
with open('madlibs.txt', 'r') as file:
    content = file.read()

# Check for words to be replaced
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
result = check.search(content)
while result:
    word = result.group()
    if word[0]  == 'A':
        print(f'Enter an {word.lower()}:')
    else:
        print(f'Enter a {word.lower()}:')
    # Replace word
    userWord = input()
    content = check.sub(userWord, content, 1)
    result = check.search(content)
# Print result
print(content)

# Save result in a new text file
print('Name your file:')
fileName = input()
with open(fileName, 'w') as newFile:
    newFile.write(content)
