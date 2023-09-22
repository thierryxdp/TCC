def filtraMultiplos(lista,numero):
    '''Função que recebe uma lista e um número e retorna todos os
    	seus múltiplos presentes na lista.
    	list,int -> list'''
    listamultiplos=[]
    posicao=0
    while posicao<len(lista):
        if lista[posicao]%numero==0:
            listamultiplos=listamultiplos+[lista[posicao]]
        posicao=posicao+1
    return listamultiplos