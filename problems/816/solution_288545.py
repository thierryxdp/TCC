def maiores(lista, n):
    """função recebe lista e ńumero inteiro e retorna
lista com elementos da entrada a partir do n ́umero inteiro
list, int--> list"""
    
    if n in lista:
        
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]
        
        return lista1
    
    else:
        
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]
        
        return lista1