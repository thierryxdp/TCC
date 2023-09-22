def faltante(pecas):
    '''retorna o numero da peca que esta faltando 
    no quebra cabeca de Joaozinho; list -> int''' 
    i=0
    while i<len(pecas):
        if pecas[i]-(i+1)!=0:
            return i+1
        i=i+1