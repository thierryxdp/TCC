def insere(lista_numero,n):
    """Dada uma lista ordenada de forma crescente de números inteiros e um número inteiro 
    'n', a função retorna uma outra lista com 'n' incluido em uma posição que mantenha 
    a lista na ordenada;
    list, int -> list"""
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero