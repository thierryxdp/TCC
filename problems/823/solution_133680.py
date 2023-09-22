def faltante(lista_n):
    list.sort(lista_n)
    ultimo_numero = lista_n[-1]
    numero_faltando = 0
    soma_do_ultimo_n = sum(list(range(ultimo_numero + 1)))
    soma_da_lista = sum(lista_n)
    while resultado == 0:
        numero_faltando = soma_do_ultimo_n - soma_da_lista
    return numero_faltando