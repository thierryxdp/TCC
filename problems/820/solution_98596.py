def posLetra(string:str,letra:str,numero:int):
    '''função que recebe uma string,uma letra e um numero inteiro
    que indica a ocorrência desejada da letra como parametros e
    retorna em que posição da string aquela ocorrência da letra está
    str,str,int->int'''
    posicao=0
    ocorrencias=0
    while posicao<len(string):
        if string.count(letra)<numero:
            return -1
        elif letra in string[posicao]:
            ocorrencias=ocorrencias+1
            if ocorrencias==numero:
                return posicao
        posicao=posicao+1