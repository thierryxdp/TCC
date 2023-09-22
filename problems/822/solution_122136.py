def repetidos(ListaR):
    '''Essa função recebe uma lista de numeros como entrada, e retorna o numero de 
    vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont