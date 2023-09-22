def qtd_divisores(n):
    """função que calcule quantos divisores um número tem; int-> list"""
    s=[]
    i=0
    for i in range(1,n+1):
        if n%(i)==0:
            s.append(n)
    return len(s)