#Start your python function here
def filtra_pares(t):
    """funcao que dada uma tupla com quatro elementos
    retorna uma tupla com os elmentos que forem par  .
    Entrada--tupla, saida--tupla"""
    s1=int(t[0])
    s2=int(t[1])
    s3=int(t[2])
    s4=int(t[3])
    if s1%2==0 and s2%2==0 and s3%2==0 and s4%2==0:
        return t
    elif s1%2!=0:
        t[1],t[2],t[3]