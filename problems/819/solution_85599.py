def filtraMultiplos(ls,n)
    """recebe uma lista de números e um (N) e rtorna outra lista contendo os elementos da original que foram divisiveis por n . 
    assinatura: list, int --> list"""
    final = []
    num = 0 
    while num < len (ls):
        if ls [num] % n == 0:
            final.append (ls[num])
        num += 1 
    return final