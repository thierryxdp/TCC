def repetidos(lista_numeros):
    "função que retorna o numero de vezes que um elemento da lista é igual ao elemento anterior"
    "list -> int'''
    i=1
    x=0
    while i<len(lista_numeros):
        if lista_numeros[i-1] == lista_numeros[i]:
            x=x+1 
        i=i+1
    return x