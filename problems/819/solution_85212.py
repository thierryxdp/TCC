filtraMultiplos(lista,n):
    """recebe uma tupla não vazia de inteiros e retornauma tupla com inteiros pares da tupla original"""
    multiplos = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos = multiplos + [lista[proximo]]
            proximo = proximo + 1
            return multiplos