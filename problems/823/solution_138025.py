def faltante(lista):
    ''' Essa função tem como objetivo identificar a peça faltante em um
    quebra cabeça, dado uma lista com as numerações das peças.'''
    
    falta = len(lista)+1
    i = 0
    n = 1
    while i <= falta:
      	if n != lista[i]:
            return i
        	i = i+1
            n = n+1