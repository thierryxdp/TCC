def faltante(lista:list) -> int:
    """Dada uma lista de números inteiros,a função
    retorna o número desse intervalo que está faltando."""
    i = 0
    list.sort(lista)
    seq_completa = list(range(1,(lista[-1]+2)))
    n_faltando = 0
    
    while n_faltando == 0:
        if seq_completa[i] not in lista:
            n_faltando = seq_completa[i]
        i += 1
        
    return n_faltando