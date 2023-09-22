def filtraMultiplos(lista:list,n:int) -> list:
    """Dada uma lista de números e um numero n, a função
    retorna os números da lista informada divisíveis por n."""
    i = 0
    divisiveis = list()
    
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(divisiveis,lista[i])
        i+=1
        
    return divisiveis