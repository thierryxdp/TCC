def maiores(listani,n):
    """A função recebe uma lista de números inteiros e um
    número inteiro 'n' como entrada. E retorna outra lista,
    que possui somente valores acima de n.
    Entrada: List, Int
    Saída: List"""
    
    list.sort(listani)
    
    if n > max(listani):
        return []
    elif n < min(listani):
        return listani
    else:
        list.append(listani,n)
        list.sort(listani)
        del(listani[:(list.index(n,listani))])
        return listani