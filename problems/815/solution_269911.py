def insere(lista_numero,n):
    '''recebe uma lista de numeros ordenados no 1 arg e retorna 
    uma lista tambem ordenada com o segundo arg adicionado
    list , complex -> list'''
    
    mlista = lista_numero
    
    nova_lista = list.append(mlista,n)
    
   	list.sort(nova_lista)
    
    return nova_lista