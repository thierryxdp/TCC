def filtraMultiplos(lista,n):
    '''Fazer uma funcao que filtre os multiplos de um numero n;
    list, int -> list'''
    
    posicao = 0
    novaLista = [ ] 
    
    while posicao < len(lista):
        if lista[posicao]%n = 0:
            novaLista = novaLista + [lista[posicao],]
        posicao = posicao + 1
    return novaLista