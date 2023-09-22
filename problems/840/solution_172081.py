def bolos(a,b,c):
    """Retorne a quantidade máxima de bolos que João consegue fazer;
    int,int,int -> int"""
    trigo = a // 2
    ovo = b // 3
    leite = c // 5
    if trigo <= ovo and trigo <= leite:
        return trigo
    elif ovo <= trigo and ovo <= leite:
        return ovo
    elif leite <= trigo and leite <= ovo:
        return leite