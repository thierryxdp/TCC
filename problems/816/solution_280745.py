def maiores(listani,n):
    """A função recebe uma lista de números inteiros e um
    número inteiro 'n' como entrada. E retorna outra lista,
    que possui somente valores acima de n.
    Entrada: List, Int
    Saída: List"""
    
    list.sort(listani)
    
    if n < listani[0]:
        return listani
    elif n > listani[::-1]:
        del listani[:n]
        return listani
    else:
        return []