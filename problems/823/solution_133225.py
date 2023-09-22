def faltante(lista):
    '''
    Função que receb uma lista de números e retorna
    qual está faltando na sequência.
    
    list -> int
    '''
    i = 1
    while i in lista:
        i = i + 1
    return i