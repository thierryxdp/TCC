x=2
ovo=3
leite=5
def bolo(A,B,C):
    qx=int(A/x)
    qovo=int(B/ovo)
    qleite=int(C/leite)
    resultado=min(qx,qovo,qleite)
    return resultado