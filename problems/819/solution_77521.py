def filtraMultiplos(lista,numero):
    '''Retorna uma lista com todos os números da lista original que sejam divisiveis por um número;
    list,int -> list'''
    contador = 0
    mutiplos = []
    while contador < len(lista):
        if lista[contador]%numero == 0:
            mutiplos.append(lista[contador])
            contador = contador + 1 
        else:
            contador = contador + 1

    return mutiplos