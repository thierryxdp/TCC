def repetidos(lista):
    """
    Calcula a quantidade de vezes que um elemento de uma lista é igual ao
    elemento anterior.
    list -> int

    Parameters:
    lista: Parâmetro do tipo lista (list);
   
    Returns:
    A quantidade de elementos repetidos em uma lista.
    """
    
    i = 0
    contador = 0

    while i < len(lista):
        if lista[i] == lista[i-1]:
            contador += 1            
        i = i + 1

    return contador