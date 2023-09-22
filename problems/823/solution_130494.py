def faltante (lista):
    """Dada uma lista N-1 numerados de 1 a N, retorna qual
    inteiro desde intervalo está faltando.
    list -> int"""
    
    contador = 1
    numero = 0
    
    while contador <= len(lista):
        if contador not in lista:
            numero += contador
        contador = lista[contador-1]+1
    
    if numero == 0:
        numero += len(lista)+1
    
    return numero