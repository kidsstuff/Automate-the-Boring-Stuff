def listing(words):
    if (len(words) == 1):
        print(words[0])
    else:
        for i in range(len(words)):
            if i == len(words) - 1:
                print(f"and {words[i]}")
            else:
                print(f"{words[i]}, ", end='')

spam = ['apples', 'bananas', 'tofu', 'cats']
listing(spam)
listing([])
listing(['cats'])
