def repetidos (lista):
    """Função que recebe uma lista de numeros e retorna o numero
    de vezes que um elemento da lista é igual ao anterior.
    list -> int"""
    
    indice = 0
    contador = 0
    numerodevezes = 0
    
    while contador < len(lista):
        
        if lista [indice] == lista [indice - 1]:
            numerodevezes += 1
            
        indice += 1
        contador += 1
    
    return numerodevezes