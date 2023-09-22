def filtramultiplos(ls,n)
    """recebe uma lista de numeros e um número(n) 
    retorna outra lista contendo os elementos da 
    original que forem dividisiveis pelo numero n. 
    assinatura: list, int --> list"""
    final = []
    num = 0 
    while num < len (ls):
        if ls [num] % n == 0:
            final.append (ls[num])
        num += 1
    return final