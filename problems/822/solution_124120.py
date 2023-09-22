def repetidos(lista:list) -> int:
    """Dada uma lista de números, a função retorna o
    número de vezes que um elemento é igual ao anterior."""
    i = 1
    repeticoes = 0
    
    while i < len(lista):        
        if lista[i] == lista[i-1]:
            repeticoes +=1
        i += 1
    
    return repeticoes