def repetidos (lista):
    
    '''recebe uma lista e retorna a quantidade de vezes um elemento da lista original é igual ao anterior.
    list -> int'''
    
    proximo = 0
    qtd_vezes  = 0
    while proximo < len(lista):
        if lista[n] == lista[(n-1)]:
            qtd_vezes = qtd_vezes + 1
        proximo  = proximo + 1
    return qtd_vezes