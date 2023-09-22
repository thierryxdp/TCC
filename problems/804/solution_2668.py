#Start your python function here
#Start your python function here
def filtra_pares(tupla):
    """ Funcao recbe uma tupla com quatro elementos inteiros e retorna uma
    nova tupla com apenas os elemtnos pares da tupla original, na mesma
    ordem em que se encontravam """
    
    n1 = tupla[0]
    n2 = tupla[1]
    n3 = tupla[2]
    n4 = tupla[3]
    
    t1 = ()
    t2 = ()
    t3 = ()
    t4 = ()
    t5 = ()
    
    if n1%2 == 0:
        t2 = t1 + (n1,)
    else:
        t2 = t1
    
    if n2%2 == 0:
        t3 = t2 + (n2,)
    else:
        t3 = t2
        
    if n3%2 == 0:
        t4 = t3 + (n3,)
    else:
        t4 = t3
        
    if n4%2 == 0:
        t5 = t4 + (n4,)
    else:
        t5 = t4
        
    return t5