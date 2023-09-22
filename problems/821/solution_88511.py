def fatorial(numero: int) -> int:
    """Calcula e retorna o fatorial de um número dado."""
    
    lista_num = list(range(numero + 1))
    fatorial = [1]
    i = len(lista_num) - 1

    while ( lista_num[i] != 1):
        fatorial[0] = list.pop(lista_num) * fatorial[0]
        i -= 1

    return fatorial[0]