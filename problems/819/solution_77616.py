def filtraMultiplos(lista:list,numero):
    '''função que dado uma lista e um número inteiro como parametros irá retornar uma nova lista
    como os múltiplos de 'numero'
    list,int->list'''
    posicao=0
    multiplos=[]
    while posicao<len(lista):
        if lista[posicao]%numero==0:
            multiplos=multiplos+(lista[posicao])
        posicao=posicao+1
    return multiplos