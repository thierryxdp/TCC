#int,int,int,int->int
def filtra_pares(e1, e2, e3, e4):
    '''dada quatro elementos de entrada, verifica os pares e os introdux a uma nova
    	tupla'''
    nv_tupla=()
    if e1%2 ==0:
        nv_tupla=nv_tupla +(e1,)
    if e2%2 ==0:    
        nv_tupla=nv_tupla +(e2,)
    if e3%2 ==0: 
        nv_tupla=nv_tupla +(e3,)
    if e4%2 ==0:
        nv_tupla=nv_tupla +(e4,)
        return nv_tupla
    elif not(e1%2 ==0) or not(e2%2 ==0) and not(e3%2 ==0) and not(e4%2==0):
        return "não há pares na tupla"