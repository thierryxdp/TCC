def intercala(l1,l2):
    '''Função que intercala os elementos das listas l1 e l2, ambas de tamanho 3'''
    '''list->list'''
    lista_nova=list(l1[0])+list(l2[0])+list(l1[1])+list(l2[1])+list(l1[2])+list(l2[2])
    return lista_nova