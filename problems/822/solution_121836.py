def repetidos(lista_num):
    """Dada uma lista de números, a função retorna o número de vezes que
    um elemento da lista é igual ao elemento anterior;
    list -> int"""
    i = 0
    soma = 0
    while i<len(lista_num):
        if lista_num[i] == lista_num[i-1]:
            soma = soma + 1
        i = i + 1
    return soma