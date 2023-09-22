def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de números e um número (n), e
       filtra todos os numero da lista que são multiplos de n;
       list,int -> list
    '''
    multiplos = ()
    prox = 0
    while prox <len(lista):
        if lista[prox]/n == prox//n:
            multiplos = multiplos + (lista[prox],)
            prox = prox + 1
        return multiplos