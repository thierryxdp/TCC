def hashtag(s):
    '''Função que recebe uma string e insere o caractere # no inicio,
    no meio e no final dela.
    str -> str
    '''
    caracteres= len(s)
    meio= caracteres//2
    meio1= s[0:meio]
    meio2= s[meio:caracteres]
    return '#' + meio1 + '#' + meio2 + '#'