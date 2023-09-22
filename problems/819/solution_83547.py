def filtraMultiplos(lista,n):
    """
    Essa função, dados uma lista e um numero n como argumentos,
    ira retornar a mesma lista contendo todos os elementos originais
    da lista que forem divisiveis por n 
    list,int->list
    """
    acumulador = 0
    nova_lista = []
    
    while acumulador <= len(lista) - 1:
        if lista[acumulador] % n == 0:
            list.append(nova_lista,lista[acumulador])
        acumulador = acumulador + 1
    return nova_lista