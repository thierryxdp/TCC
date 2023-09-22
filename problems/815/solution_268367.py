def insere(lista,n):
    """funcao que insere o numero n na lista fornecida ja na ordem
       crescente
       
       lista, int-> lista
    """
    
    lista_1 = list.insert(lista,n,0)
    
    return list.sort(lista_1)