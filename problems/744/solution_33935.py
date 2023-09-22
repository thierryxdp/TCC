def hashtag(s):
    '''funcao que dado um texto ela retorna o mesmo texto
 com uma # no inicio, meio e fim; str -> str'''
    quantidade = len(s)
    meio = int((quantidade/2))
    return '#' + s[0:meio] + '#' + s[meio:] + '#'