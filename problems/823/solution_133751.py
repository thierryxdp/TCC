def faltante(lista_de_n):
    '''Função que recebe uma lista de numeros inteiros, lista_de_n, representando as peças do quebra-cabeças, e retorna o numero desse intervalo que falta'''
    ''' list -> int'''
    i = 0
    list.sort(lista_de_n)
    n_faltantes = 0
    while i < len(lista_de_n):
        if lista_de_n[i] - i == 2:
            n_faltantes += 1
        i += 1
    if n_faltantes == 0:
        return lista_de_n[-1] + 1
    else:
        return lista_de_n[-1] - n_faltantes