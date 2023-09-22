def repetidos(lista):
    """unção que retorna o número de vezes que um elemente da lista é igual
    ao elemento anterior através da entrada lista;
    Entrada: list
    Saída: int"""
    a = 0	
    b = 0
    
    while a < len(lista):
        if lista[a] == lista[a - 1]:
            b = b + 1
        a = a + 1
    return b