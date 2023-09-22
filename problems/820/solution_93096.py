def posLetra (string, letra, aparicao):
    ''' função que procura dentro de uma string a letra fornecida
        e retorna seu índice, considerando qual ocorrência de
        entrada foi fornecida, assim o indice da aparição desejada
        [str,str,int--int]'''

    
    SL = str.split(string)
    texto = string
    indice = 0
    ocorrencia = 0
    

    if string.count(letra)< aparicao:
        return -1
    
    else:
        while ocorrencia < aparicao:
            if texto[indice] == letra:
                ocorrencia += 1
            indice += 1

    return indice - 1