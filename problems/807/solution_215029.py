def conta_frases(text):
    num=text.count('...')*(-2)
    num+=text.count('.')
    num+=text.count('!')
    num+=text.count('?')
    if num==0:
        num+=1
        return num
    else:
        return num