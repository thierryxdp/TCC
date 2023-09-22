def maiores(lista,n):
    """Finção que dado uma lista retorna , os numeros maiores que n da lista
    list -> list"""
    if n not in lista:
        list.append(lista,n)
        
        list.sort(lista)
        indices= list.index(lista,n)
        
        fatiado = lista[indice+1:]
        
        return fatiado