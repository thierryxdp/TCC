def faltante(pecas):
    '''retorna o numero da peca que esta faltando 
    no quebra cabeca de Joaozinho; list -> int''' 
    i=1
    while i<len(pecas):
        if pecas[i-1]!=i:
            return i
        else:
            return int(pecas[-1]+1)
        i=i+1