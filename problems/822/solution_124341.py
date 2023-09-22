def repetidos(lista_numeros):
    """A função recebe uma lista de números como parâmetro,
    e deve retornar o número de vezes que um elemento da lista
    é igual ao elemento anterior.
    Entrada: List
    Saída: Int"""
    
    i = 0
    antecessor = i-1
    sucessor = i+1
    igual = 0
    
    while lista_numeros[i] == lista_numeros[antecessor] or lista_numeros[i] == lista_numeros[0][sucessor]:
        igual = igual + i
        i=i+1
    return antecessor