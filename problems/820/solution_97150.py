def posLetra(string:str,letra:str,numero:int):
    '''função que recebe uma string,uma letra e um numero inteiro
    que indica a ocorrência desejada da letra como parametros e
    retorna em que posição da string aquela ocorrência da letra está
    str,str,int->int'''
    posicao=0
    frase=string
    while posicao<len(string):
        if letra in string:
            frase=frase.count(letra)
        posicao=posicao+1
        elif str.count(letra)<numero:
            return -1
    return frase