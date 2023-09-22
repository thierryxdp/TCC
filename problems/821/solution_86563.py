def fatorial(n):
    """Retorna o fatorial do numero n;
       Entrada: int;
       Saida: float;
    """
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return n*(n-1)
    if n==3:
        return n*(n-1)*(n-2)
    if n==4:
        return n*(n-1)*(n-2)*(n-3)
    if n==5:
        return n*(n-1)*(n-2)*(n-3)*(n-4)
    if n==6:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)
     if n==7:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)
     if n==8:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)
    if n==9:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)