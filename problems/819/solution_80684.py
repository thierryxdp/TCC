def filtraMultiplos(lNumeros,n):
    '''Retorna uma lista com os elementos da lista de entrada
       que forem múltipos do número de entrada;
       list, int -> list'''
    count=0
    lMultiplos=[]
    while count < len(lNumeros):
        if lNumeros[count]%n==0:
            lMultiplos.append(lNumeros[count])
        count+=1
    return lMultiplos