def lingua_p(palavra):
    
    vogal = 'aeiouAEIOUáàâãÁÀÃÂéèÉÈíìÍÌóòôõÓÒÕÔúùÚÙ'
    contador = 0
    
    for i in range(len(palavra)):
        indice = i + contador
        if palavra[indice] in vogal:
            palavra = palavra[:indice+1] + 'p' + palavra[indice:]
            contador += 2
    
    return palavra