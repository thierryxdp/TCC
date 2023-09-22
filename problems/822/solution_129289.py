def repetidos(lista):
    """Retorna a quantidade de vezes em que dois numeros consecutivos sao iguais na lista;
    list -> int"""
    numero_anterior = lista[0]
    x = 1
    vez = 0
    while x < len(lista):
        if lista[x] == numero_anterior:
            vez += 1
        numero_anterior = lista[x]
        x += 1
    return vez