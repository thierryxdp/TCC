def repetidos(num):
    
    """
    lista--->int
    i e repeticoes sao iniciados em 0 e enquanto i for menor que o tamanho
    da lista, são feitas somas de 1 para cada valor que seja igual ao
    anterior, pedindo o retorno da quantidade de repeticoes
    
    """
    
    i=0
    reps=0
    
    while i<len(num):
        
        if num[i]==num[i-1]:
            reps+=1
        i+=1
    
    return reps