def repetidos(lista):
    """Recebe como entrada uma lista de números, e retorna o número 
    de vezes que um elemento da lista  ́e igual ao elemento anterior"""
    """list -> int"""
    contador = 0
    i = 0
    
    while (i < len(lista)):
        if lista[i] == lista[i]:
            contador +=1
            
    i = i + 1
    return contador