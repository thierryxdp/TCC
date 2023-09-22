def faltante (lista):
    """Função que dada uma lista de tamanho N -1, retorna o numero faltante no intervalo [1,N];
       list -> int."""
    list.sort (lista)
    i = 1
    while i  in lista:
        i = i + 1
    return i