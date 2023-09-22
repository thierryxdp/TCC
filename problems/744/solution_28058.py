def hashtag(s):
    '''dada uma string s, retorna a string s acrescida de '#' no início,
    meio e fim dela; str -> str'''
    i = len(s)//2
    n = len(s)%2
    if n == 0:
        return '#' + s[0:i] + '#' + s[i:] + '#'
    elif n == 1:
        return '#' + s[0:i] + '#' + s[i:] + '#'