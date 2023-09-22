def hashtag(s):
    '''Funcao recebe uma string e coloca hastag no inicio meio e fim da string
string -> string'''
    qnt_letras = len(s)//2
    parte1 = s[:qnt_letras]
    parte2 = s[qnt_letras:]
    return '#' + parte1 + '#' + parte2 + '#'