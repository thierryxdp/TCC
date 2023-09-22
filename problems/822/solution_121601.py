def repetidos(lista):
    '''retorna o número de vezes que um elemento da lista de entrada é igual
    ao anterior;
    list -> int'''
    
    elemento = 1
    repeticoes = 0
    
    while elemento < len(lista):
        if lista[elemento] == lista[elemento-1]:
            repeticoes += 1
        elemento += 1
        
    return repeticoes