def filtraMultiplos (lista_num,n):
    """Função que recebe uma lista de números e um número n e retorna uma lista com os números
    da lista dada que são múltiplos no número n dado.
    list, int -> list"""
    i = 0
    multiplos = []
    while i < len(lista_num):
        if lista_num[i]%n==0:
            multiplos = multiplos + [lista_num[i]]
        i = i+1
    return multiplos