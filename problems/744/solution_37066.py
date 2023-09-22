def hashtag(s):
    quantidade = len(s)
    if quantidade % 2 == 0:
        inicio = s[:(len(s)//2)+1]
        fim = s[(len(s)//2):]
        s1 = '#' + inicio + '#' + fim + '#'
        return s1