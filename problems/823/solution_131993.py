def faltante(pecas):
    '''retorna o numero da peca que esta faltando 
    no quebra cabeca de Joaozinho; list -> int''' 
    i=1
    while i<len(pecas):
        if pecas[i]!=i:
            return i
        i=i+1