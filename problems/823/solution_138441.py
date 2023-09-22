def faltante(lista):
    '''Recebe como entrada uma lista de N-1 números inteiros, 
    no intervalo de 1 a N, e retorna o número faltante.
    list[int] -> int'''
    lista.sort()
    posicao=0
    achou=False
    valor_anterior,valor=0,0
    while (posicao<=len(lista))and(achou==False):
        if posicao==len(lista):
           return len(lista)+1
        else:
            valor=lista[posicao]
            if valor==valor_anterior+1:
                valor_anterior=valor
            else:
                achou=True
                return valor-1
        valor=valor+1
        posicao=posicao+1