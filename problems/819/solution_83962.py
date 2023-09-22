def filtraMultiplos(lista,n):
    '''função que retorna lista com números 
       multiplos do numero n, dados lista e o número n;
       list, int => list'''
        
    final = []
    contador = 0
    while (contador < len(lista)):
           if lista[contador] % n == 0:
                final = final+[lista[contador],]
            contador = contador + 1
    return(final)