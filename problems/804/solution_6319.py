def filtra_pares(elementos):
    """Função que retorna apenas os números inteiros pares do conjunto;
    tuple -> tuple"""
    tupla_vazia = ()
    if elementos[0] % 2 == 0:
        tupla_vazia = tupla_vazia + (elementos[0],)
    if elementos[1] % 2 == 0:
        tupla_vazia = tupla_vazia + (elementos[1],)
    if elementos[2] % 2 == 0:
        tupla_vazia = tupla_vazia + (elementos[2],)
    if elementos[3] % 2 == 0:
        tupla_vazia = tupla_vazia + (elementos[3],)
    
    return tupla_vazia