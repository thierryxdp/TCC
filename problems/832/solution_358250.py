def eh_quadrada(lista):
    '''Função que identifica se uma matriz é quadrada ou não.
    lista->bool'''
       lista=[]
    for i in range(len(lista)):
    	linha=len(lista)
        coluna=len(lista[i])             
        if linha == coluna:
            return True
        elif not lista:
            return True
        else:
            return False