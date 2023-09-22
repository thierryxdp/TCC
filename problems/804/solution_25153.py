'''recebe uma tupla t e retorna uma nova tupla contendo os elementos pares da tupla t
Assinatura: tuple -> tuple'''
def resto(x,y):
    return x%y
def filtra_pares(t):
    l=[]
    if resto(t[0],2)== 0:
        list.append(l, t[0]) 
    if resto(t[1],2)== 0:
        list.append(l, t[1])
    if resto(t[2],2)==0:
        list.append(l,t[2])
    if resto(t[3],2)==0:
        list.append(l,t[3])
    return tuple(l)