def hashtag(s):
    '''retorna uma string com caractere #'''
    s = 'string'
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
   
    return '#' + s1 + '#' + s2 + '#'