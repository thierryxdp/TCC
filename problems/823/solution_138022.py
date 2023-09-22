def faltante(lista):
    ''' Essa função tem como objetivo identificar a peça faltante em um
    quebra cabeça, dado uma lista com as numerações das peças.'''
    
    falta = len(lista)+1
    i = 0
    
    while i =< falta:
      	if lista[i] not in lista:
            return i
        i = i+1