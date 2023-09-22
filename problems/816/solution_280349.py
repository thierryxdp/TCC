def maiores(lista,n):
    """Retorna lista que contenha todos os números da lista de entrada que são maiiores que n.
    lista, int --> lista"""
    
    list.append(lista,n)
    
    list.sort(lista)
    
    index = list.index(lista,n)
    
    nova_lista = lista[index:]
    
    return nova_lista