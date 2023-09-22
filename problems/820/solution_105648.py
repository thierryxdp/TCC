def posLetra(frase,caracter,ocorrencia):
    '''funcao que retorna a incidencia'''
    ind = 0

    
    while ocorrencia > 0:
        if not caracter in frase:
            break
        indice = str.index(frase, caracter) + 1
        frase = frase[indice:len(frase)+1]
        ocorrencia = ocorrencia -1
        ind = ind + indice

    return ind - 1