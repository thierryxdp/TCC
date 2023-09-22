def maiores(listani,n):
    """A função recebe uma lista de números inteiros e um
    número inteiro 'n' como entrada. E retorna outra lista,
    que possui somente valores acima de n.
    Entrada: List, Int
    Saída: List"""
    
    list.sort(listani)
    
    if n > max(listani):
        return []
    else: 
        list.append(listani,n)
        list.sort(listani)
        del(listani[n:])
        return listani