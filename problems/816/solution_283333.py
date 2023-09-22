def maiores(lista,n):
    """
        Função que recebe uma lista e um numero n e retornar uma nova lista contendo apenas numero maiores que n
        (1) a lista final recebe apenas numero maiores do que n. Ela é a lista retornada pela função.

        list, int or float --> list
        
    """
    
    lista_final = []
    for i in lista:
        if i >= n:
            lista_final.append(i)
    lista_final.sort()
    return lista_final