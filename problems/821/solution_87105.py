def fatorial(n):
    """"função que calcula o fatorial de um número n.

    int -> int

    exemplos:
    fatorial(3)==6
    fatorial(2)==2
    fatorial(5)==120"""
    total=1
    while n-1!=0:
        total=total*n
        n=n-1