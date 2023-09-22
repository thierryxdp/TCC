A=int
B=int
C=int
x=2
ovo=3
leite=5
def bolos(A,B,C):
    qx=int(A/x)
    qovo=int(B/ovo)
    qleite=int(C/leite)
    q_bolo=min(qx,qovo,qleite)
    return q_bolo