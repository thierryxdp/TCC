def repetidos(lista):
    ''' Fazer uma funcao que pegue uma lista de numeros e retorne quantas vezes esse numero é igual ao anterior;
    list -> int'''
    
    i = 0
    quant_rep = 0
    
    while i < len(lista):
        if lista[i] == lista[i-1]:
            quant_rep += 1
        i = i + 1
        
    return quant_rep