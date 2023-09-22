def hashtag(s):
    quantidade = len(s)
    inicio = s[:(len(s)//2)+1]
    fim = s[(len(s)//2):]
    if quantidade % 2 == 0:
        s1 = '#' + inicio + '#' + fim + '#'
        return s1
    else:
        s2 = '#' +s[:(len(s)//2)+1] '#' + fim + '#'
        return s2