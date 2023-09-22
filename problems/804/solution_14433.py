def filtra_pares
	"""Funcao que recebe uma tupla com quatro elementos inteiros como paremetro 
    e retorna uma nova tupla contendo apenas os elementos pares da tupla original
  	na mesma ordem em que se encontravam"""
    t = ( )
    
    if fp[0] %2 == 0:
             t = t +(fp[0],)
    else:
             t = t
    if fp[1] %2 == 0:
             t = t +(fp[1],)
    else:
             t = t
    if fp[2] %2 == 0:
             t = t +(fp[2],)
    else:
             t = t
    if fp[3] %2 == 0:
             t = t +(fp[3],)
    else:
             t = t
    return t