def filtraMultiplos(lista, n):
    '''Funcao recebe uma lista de numeros e um numero e retorna todos os números da lista que forem divisiveis por n
lis/int -> lista'''
    contador = 0
    acumulador = []
    while(contador < len(lista)):
        if (lista[contador] % n == 0):
            acumulador = [acumulador + lista[contador]
        contador +=1
    return acumulador