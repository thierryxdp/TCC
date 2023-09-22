def repetidos(lista):
    '''A função retorna a quantidade de vezes que um elemento
    da lista se repete em sequência com base no valor anterior, 
    por exemplo: 221223398422. Resposta: 4
    lista -> float'''
    
    i = 0
    quant_contados = 0
    
    while len(lista) > i:
        if lista[i] == lista[i-1]:
            quant_contados = quant_contados + 1
        i = i + 1
    return quant_contados