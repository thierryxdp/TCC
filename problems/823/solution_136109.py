def faltante (lista):
    """Função que dados n-1 inteiros numerados de 1 a N retorna qual número inteiro está faltando"""
    """lista -> int"""
    
    i = 0
    retorno = []
    
    while i < len(frase):
        n = lista[i]
    if n not in lista:
        return n 
    n += 1