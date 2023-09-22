def repetidos(lista_numeros):
    """A função recebe uma lista de números como parâmetro,
    e deve retornar o número de vezes que um elemento da lista
    é igual ao elemento anterior.
    Entrada: List
    Saída: Int"""
    
    i=0
    sucessor=i+1
    igual=0
    sorted(lista_numeros)
    
    while lista_numeros[i] == lista_numeros[sucessor]:
        igual=igual+i
        i=i+1
    return sorted(lista_numeros)