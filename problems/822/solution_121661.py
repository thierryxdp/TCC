def repetidos(lista):
    '''fução que dada uma lista de números, retorna quantas vezes um elemento da lista é igual ao elemento anterior; list->int'''
    
    anterior=0
    posterior=1
    quantidade=0

    while posterior<len(lista):
        if lista[posterior]==lista[anterior]:
            quantidade=quantidade+1
        anterior=anterior+1
        posterior=posterior+1

    return quantidade