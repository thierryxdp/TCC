def eh_quadrada(lista):
    '''Função que identifica se uma matriz é quadrada ou não.
    lista->bool'''
    lista_vazia=[]
    for i in range(len(lista)):
    	linha=len(lista)
        coluna=len(lista[i])             
        if linha == coluna:
            return True
        elif lista==lista_vazia:
            return True
        else:
            return False