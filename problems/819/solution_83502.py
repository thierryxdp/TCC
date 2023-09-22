def filtraMultiplos(lista,n):
    """
    Essa função, dados uma lista e um numero n como argumentos,
    ira retornar a mesma lista contendo todos os elementos originais
    da lista que forem divisiveis por n 
    list,int->list
    """
    acumulador = 0
    nova_lista = []
    acumulador_2 = 0
    
    while acumulador > len(lista):
        if lista[acumulador_2] % n == 0:
            list.append(nova_lista,n)
        acumudalor = acumulador + 1
        acumulador_2 = acumulador_2 + 1
       
       
    return nova_lista