def faltante (lista):
    """Função que dados n-1 inteiros numerados de 1 a N retorna qual número inteiro está faltando"""
    """lista -> int"""
    
    n = 1
    retorno = []
    
    while n < len(lista) + 1:
        n = lista[n]
    if n not in lista:
        return n 
    n += 1
    
    return n