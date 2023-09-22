def hashtag(s):
    """recebe uma string s e a retorna com o caractere # no inicio, meio e fim
    str -> str"""
    metade = len (s) //2
    tam = len(s)
    retorno = '#'+ s[0:metade] + '#' + s[metade:] + '#' 
    return retorno