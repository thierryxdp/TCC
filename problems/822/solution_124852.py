def repetidos(lista_numeros):
    """ Função que recebe como entrada uma lista de números e 
        retorna o número de vezes que um elemento da lista é
        igual ao elemento anterior;
        list(int) -> int"""
    i = 1 #representa o índice da lista_numeros
    numero_vezes = 0
    while i<len(lista_numeros):
        if lista_numeros[i] == lista_numeros[i-1]:
            numero_vezes = numero_vezes + 1
        i = i+1
    return numero_vezes