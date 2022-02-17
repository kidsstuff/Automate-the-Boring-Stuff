# Strong password: 8+ characters long, uppercase and lowercase, 1+ digit
import re
def strongPasswordDetection(password):
    passCheckRegex = re.compile(r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{8,})\S$')
    if passCheckRegex.search(password):
        print("Strong password")
        return True
    else:
        print("Weak password")
        return False

# Tests
passwords = ['123456', 'abcde', 'AbCdEfGhIj', 'Password1', '2Super2Strong3', '!2$%32asdf234234234']
for password in passwords:
    print(password)
    strongPasswordDetection(password)
