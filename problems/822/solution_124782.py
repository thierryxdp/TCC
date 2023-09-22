def repetidos(num):
    
    """Retorna o numero de vezes que um elemento é repetido numa lista"""
    
    i=1
    repetidos=0
    while i<len(num):
        if num[i] == num[i-1]:
            repetidos = repetidos +1
        i+=1
    return repetidos