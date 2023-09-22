def qtd_divisores(x):
    """Função que conta quantos divisores um número(x) tem"""
    """int->int"""
    s=0
    for y in range(x):
        if y==0:
            s=s
        elif x%y==0:
            s=s+1
    if x>0:
        return s +1
    if x<0:
        return 0