def repetidos(lista):
    '''dada uma lista de numeros (lista), retorna o numero de vezes que o elemento da lista é igual ao elemento anterior; list -> int'''
    indice = 0 
    soma = 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            soma = soma + 1
        indice = indice +1 
    return soma