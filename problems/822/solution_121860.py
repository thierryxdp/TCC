def repetidos (lista):
    """Função que, dada uma lista de números, retorna a quantidade de vezes que um elemento da lista é igual ao anterior
    entrada: list
    saída: int"""
    
    proximo = 1
    quantidade = 0
    
    while proximo < len(lista):
        if lista[proximo] == lista[proximo-1]:
            quantidade = quantidade + 1
        proximo = proximo + 1
            
    return quantidade