def maiores(lista, n):
    """Dada uma lista de numeros inteiros e um número 
    inteiro n qualquer, cria outra lista com números 
    maiores que n list, int -> list """
    if n not in lista:
        list.append(lista, n)
        
    list.sort(lista)
    indice = list.index(lista, n)
    
    lista2 = lista[indice+1:]
    return lista2