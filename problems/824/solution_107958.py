def uppCons(frase):
    """ recebe uma 'frase' e retorna a mesma frase, mas com todas as suas consoantes
    em letras maiúsculas.
    str -> str """
    lista = frase
    i = 0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            lista = lista.replace (frase[i],str.upper(frase[i])
        i = i+1
                                   
    return lista