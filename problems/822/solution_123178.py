def repetidos(lista):
    """Função que recebe como entrada uma lista de números e retorna
    o número de vezes que um elemento da lista é igual  ao elemento 
    anterior
    
    Parameters:
    lista: Lista de números que será analisada
    
    Returns:
    Retorna o número de vezes que um elemento é igual ao anterior
    list -> int
    """
    i=0
    repeticao = 0
    while i < len(lista):
        if lista[i] == lista[i+1]:
            repeticao = repeticao +1
        i+=1
    return repeticao