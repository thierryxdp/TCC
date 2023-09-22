def filtraMultiplos(numeros,n):
    '''Função que, a partir de uma dada lista de
    números, retorna os números dessa lista que 
    são divisíveis por um dado número n
    list,int->list'''
    multiplos = ()
    prox = 0
    while prox <len(numeros):
        if numeros[prox]%n == 0:
            multiplos = multiplos + numeros[prox]
        prox = prox + 1
    return multiplos