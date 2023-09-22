def filtra_pares(a,b,c,d):
    """Dado uma tupla com quatro elementos inteiros como parâmetro,
    retorna apenas os elementos pares dessa tupla, na mesma ordem;
    tuple->tuple"""
    x=a%2
    y=b%2
    z=c%2
    w=d%2
    if x!=0:
        return (b,c,d)