def filtra_pares(entrada):
    
    saida = ()
    
    if entrada[0] % 2 == 0:
    	saida = saida + (entrada[0],)
    if entrada[1] % 2 == 0:
    	saida = saida + (entrada[1],)
    if entrada[2] % 2 == 0:
    	saida = saida + (entrada[2],)
    if entrada[3] % 2 == 0:
        saida = saida + (entrada[3],)
        
    return saida