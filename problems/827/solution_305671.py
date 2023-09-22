def qtd_divisores(n):
    """função que calcule quantos divisores um número tem; int-> list"""
    s=[]
    x=0
    for i in range(1,n+1):
        if n%(n+1)==0:
            x=x+1
            s.append(n)
    return len(s)