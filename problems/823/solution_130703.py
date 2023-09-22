def faltante(lista):
    '''Dado uma lista de numeros de 1 a N, retorna qual numero, dentro deste intervalo, esta faltando na lista.
    list -> int'''
    atual = 1
    i = 0

    lista.sort()
    if lista[0] != 1:
        return 1
    while i <= len(lista):
        if lista[i] != atual:
            return atual
        atual += 1
        i += 1
    return atual