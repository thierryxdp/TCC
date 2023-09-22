def hashtag(s):
    """Função que insere o caractere (#) no inicio, meio e fim da string (s).
    str -> str"""

    metade1 = '#' + s[0:int(len(s)/2)]
    metade2 = s[int(len(s)/2):] + '#'
    
    return metade1 + '#' + metade2