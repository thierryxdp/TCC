def filtra_pares (t0,t1,t2,t3):
    ''' função que ao receber a sequência de uma tupla formada por quatro
        elementos inteiros, retorna uma nova tupla composta pelos elementos
        pares da tupla inicial
        int-->int'''
    
    novatupla = ()
    if t0 % 2 == 0:
        novatupla = novatupla + (t0,)
        
    
    if t1 % 2 == 0:
        novatupla = novatupla + (t1,)
        
     
    if t2 % 2 == 0:
        novatupla = novatupla + (t2,)
       
    
    if t3 % 2 == 0:
        novatupla = novatupla + (t3,)

        return novatupla