def colchao(medidas,H,L):
    """ Dada as medidas da porta e de um colchao, retorna se é possivel passar o colchao pela porta ou não """
    medidas= [a,b,c]
    if (a>b):
        aux=a
        b=a
        b=aux
    elif (b>c):
        aux=b
        b=c
        c=aux
    elif (a>b):
        aux=a
        a=b
        b=aux
    if (L>H):
        aux=H
        H=L
        L=aux
    if (L>=a and H>=b):
        return True
    else:
        return False