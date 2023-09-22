def posLetra(string:str,letra:str,numero:int):
    '''função que recebe uma string,uma letra e um numero inteiro
    que indica a ocorrência desejada da letra como parametros e
    retorna em que posição da string aquela ocorrência da letra está
    str,str,int->int'''
    posicao=0
    contador=0
    while posicao<len(string):
        if letra==string[posicao]:
            contador=contador+1
            if contador==numero:
                return posicao
        elif string.count(letra)<numero:
            return -1
        posicao=posicao+1