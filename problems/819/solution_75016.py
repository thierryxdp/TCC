def filtraMultiplos (lista_numeros, n):
    """Função que, dados uma lista com números e um número, deve retornar outra lista contendo todos os elementos da lista original que forem divisíveis por n
    entrada: list, int
    saída: list"""
    
    divisiveis = ()
    proximo = 0
    
    while proximo < len(lista_numeros):
        if lista_numeros[proximo] % n == 0:
            divisiveis = divisiveis + (lista_numeros[proximo],)
        proximo = proximo + 1
        
    return divisiveis