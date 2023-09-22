def filtra_pares(x):
    ''' Essa função recebe uma tupla com 4 valores e retorna 
    	uma tupla com os valores pares
        tupla -> tupla'''
    a,b,c,d = x #separa os itens da tupla
    y = ()		#tupla vazia pra receber os valores necessarios
    
    if (a/2) == (a//2):
        y = (a,)
    if (b/2) == (b//2):
        y = y+(b,)
    if (c/2) == (c//2):
        y = y+(c,)
    if (d/2) == (d//2):
        y = y+(d,)
    return y