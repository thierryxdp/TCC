def faltante(pecas):
    '''retorna o numero da peca que esta faltando 
    no quebra cabeca de Joaozinho; list -> int''' 
    i=0
    lista=pecas[:]
    lista.sort
    while i<len(pecas):
        if (lista[i]+1)!=(lista[i+1]):
            return int(lista[i])
        i=i+1