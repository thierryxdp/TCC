def hashtag (s):
    '''Função que retorna # no inicio, meio e final da string
        str -> str'''
    return '#' + s[:len(s)//2:] + '#' + s[len(s)//2:] + '#'