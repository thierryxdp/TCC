def filtraMultiplos(lista_num: list, n :float) -> list:
    """Retorna uma lista contendo os elementos da lista de
    entrada que são divisíveis pelo número n."""
    
    div_por_n = list()
    i = 0
    
    while (i < len(lista_num)):
        if lista_num[i] % n == 0:
            list.append(div_por_n,lista_num[i])
        i += 1
        
    return div_por_n