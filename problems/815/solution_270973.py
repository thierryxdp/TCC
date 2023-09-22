# Dada uma lista ordenada e um número, queremos 
# nova lista ordenada contendo o número.
# Resolução:
# 1. Acrescenta o número à lista através do list.append();
# 2. Então, ordena os elementos da lista usando list.sort();
# 3. Devolve

def insere(lista_numero: list, n: int) -> list:
    '''Dada uma lista ordenada e um número, devolve 
    nova lista ordenada contendo o número'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero