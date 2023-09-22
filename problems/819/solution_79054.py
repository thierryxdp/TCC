def filtraMultiplos(lista:list,n:int)-> bool:
    ''''Filtra os múltiplos de um número n contidos na lista recebida'''''
    return list(filter(lambda numeros: numeros % n == 0, lista))