def repetidos (lista_numeros):
    """Função que, dada uma lista de números, retorne o número de vezes que um elemento da lista é igual ao elemento anterior
    entrada: list
    saída: int"""
    
    proximo = 0
    
    while proximo < len(lista_numeros):
        if lista_numeros[proximo] == lista_numeros[proximo - 1]:
            proximo = proximo + 1
            
        if lista_numeros[proximo] != lista_numeros[proximo - 1]:
            proximo = proximo
            
    return proximo