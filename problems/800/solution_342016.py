def total(lista, dicionario):
    """Retorna um inteiro que é o total da lista de compras dada
    entrada, baseado nos valores de um dicionário que possui os 
    produtos da loja como chaves.
    list, dict -> int"""
    T = 0
    for compras in lista:
        T+=dicionario[compras]
    return round(T,2)