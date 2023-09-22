def posLetra(frase,caracter,ocorrencia):
    '''funcao que retorna a posiçao em que a recorrencia da letra esta, dado a frase, o carcater e a ocorrencia
    '''
    ind = 0

    
    while ocorrencia > 0:
        if not caracter in frase:
            
            return -1
        indice = str.index(frase, caracter) + 1
        frase = frase[indice:len(frase)+1]
        ocorrencia = ocorrencia -1
        ind = ind + indice

    return ind - 1