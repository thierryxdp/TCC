def uppCons(frase):
    '''Funcao que recebe uma frase e retorna a mesma frase com todas as consoantes
em letras maiusculas, sendo esta a unica alteracao.
Str -> Str'''
    indice = 0
    frase_upper = ''
    while indice<len(frase):
        if frase[indice] not in 'aeiouãáâéíóõú':
            frase_upper = str(frase_upper) + str.upper(frase[indice])
        else:
            frase_upper = str(frase_upper) + frase[indice]
        indice = indice + 1
    return frase_upper