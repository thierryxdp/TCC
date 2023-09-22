def posLetra (string,letra,n):
    '''Função que retorna em que posição da string a letra está.
    str,str,int->int'''
    i = 0
    posicao = 0
    ocorrencia = 0
    
    lista = list(string)
    while i < len(lista):
        if lista[posicao] == letra:
            ocorrencia += 1
            if ocorrencia == n:
                return posicao
        i += 1
        posicao += 1
    return -1