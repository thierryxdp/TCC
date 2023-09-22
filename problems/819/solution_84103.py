def filtraMultiplos(ls,n):
    """recebe uma lista de números e um número (n) e 
    retorna outra lista contendo os elementos da lista 
    original que forem divisiveis pelo númerto n.
    assinatura: list, int --> list"""
    final = []
    num = 0
    while num < len(ls):
        if ls [num] % n == 0:
            final.append (ls[num])
        num += 1
    return final