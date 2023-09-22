def filtra_pares (tuplainicial):
    ''' função que ao receber a sequência de uma tupla formada por quatro
        elementos inteiros, retorna uma nova tupla composta pelos elementos
        pares da tupla inicial
        tupla-->int'''
    
    novatupla = ()
    if tuplainicial[0] % 2 == 0:
        novatupla = novatupla + (tuplaicial[0],)
        
    
    if tuplainicial[1] % 2 == 0:
        novatupla = novatupla + (tuplainicial[1],)
        
     
    if tuplainicial[2] % 2 == 0:
        novatupla = novatupla + (tuplainicial[2],)
       
    
    if tuplainicial[3] % 2 == 0:
        novatupla = novatupla + (tuplainicial[3],)

        return novatupla