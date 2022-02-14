import re
def myStrip(text, chars=r' '):
    for x in chars:
        if x in ['*','+','.','?','|','[',']','{','}','^', '$']:
            regex = re.compile('\\' + x)
        else:
            regex = re.compile(x)
        text = regex.sub('', text)
    return text

print(myStrip(',,,,,rrttgg.....banana....rrr', ',.grt'))
