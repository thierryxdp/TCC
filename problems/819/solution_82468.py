def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de números e um número (n), e
       filtra todos os numero da lista que são multiplos de n;
       list,int -> list
    '''
    multiplos = ()
    seguinte = 0
    while seguinte <len(lista):
        if lista[seguinte]%n == 0:
            multiplos = multiplos + (lista[seguinte],)
        seguinte = seguinte + 1
    return list(multiplos)