#Start your python function here
def filtra_pares(t):
    """funcao que dada uma tupla com quatro elementos
    retorna uma tupla com os elmentos que forem par  .
    Entrada--tupla, saida--tupla"""
    s1=int(t[0])
    s2=int(t[1])
    s3=int(t[2])
    s4=int(t[3])
    if (s1+s2+s3+s4)%2==0:
        return t