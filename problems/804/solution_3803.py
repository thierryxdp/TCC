def filtra_pares(tupla)
    """Recebe quatro números inteiros e retorna apenas os pares.
    tupla(int,int,int,int) -> tupla"""
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    
    if int(a)%2==0 and int(b)%2==0 and int(c)%2==0 and int(d)%2==0:
        return (a,b,c,d)