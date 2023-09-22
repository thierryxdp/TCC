def faltante(lista):
    """retorna o numero fora da lista correspondente a uma peça faltante; list -> int"""
    a=list.sort(lista)
    b=1
    while b<=len(lista):
        if a[b]-a[b-1]>1:
            return a[b-1]+1
        else:
            b+=1