def posLetra(frase,letra,num):
    '''funcao que recebe como entrada uma frase, uma letra
    e o número de ocorrencias desejada dessa letra e retorna a posição
    dessa ocorrencia na frase.
    entradas: str, str,int
    saida: int
    '''
    if str.count(frase,letra)>= num:
        return str.index(frase,letra,-1,)
    else:
        return -1