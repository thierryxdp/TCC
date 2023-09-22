def repetidos (lista):
    """que receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista é igual ao elemento anterior.
    Exemplo: repetidos([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]) 
    Resposta: 6.
    entrada->list
    retorna-> int"""
    
    resposta=0
    indice=1
    
    while indice<len(lista):
        if lista [indice]== lista[indice-1]:
            resposta= resposta+1
            indice =indice +1
        elif lista [indice]!= lista [indice-1]:
            indice =indice+1
        
    return resposta