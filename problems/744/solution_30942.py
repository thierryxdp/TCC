def hashtag(s):
    '''retorna o fatiamento da string s mais o caractere #'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s