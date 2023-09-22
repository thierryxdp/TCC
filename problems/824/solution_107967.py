def uppCons(frase):
    """ recebe uma 'frase' e retorna a mesma frase, mas com todas as suas consoantes
    em letras maiúsculas.
    str -> str """
    atualizada = frase
    i = 0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiouÃÁÉÍÚãéíóú':
            atualizada = atualizada.replace (frase[i],str.upper(frase[i]))
        i = i+1
                                   
    return atualizada