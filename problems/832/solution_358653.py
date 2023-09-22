def ehquadrada(a):
    """Funcao que, ao receber uma matriz, retorna True se for quadrada e False caso contrario
    list -> bool"""
    for i in range(len(a)+1):
        if len(a)==len(a[i]):
            return True
        elif len(a)==1:
            return False
        else:
            return False