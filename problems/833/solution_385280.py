def conta_numero(numero,matriz):
    """retorna quantas vezes numero aparece na matriz;
    int, list(list) -> int"""
    c=0
    i=0
    linha=matriz[i]
    for x in linha:
        if x==numero:
            c=c+1
        i=i+1
    return c