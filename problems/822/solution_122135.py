def repetidos(ListaN):
    '''Essa função recebe uma lista de numeros como entrada, e retorna o numero de 
    vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    contador = 0
    j = 1
    while j < len(listaN):
        if listaN[j] == (listaN[j-1]):
            listaN.count(listaN[j])
            contador += 1
        j += 1
    return contador