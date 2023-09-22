# Dada uma lista de inteiros e um inteiro n, queremos
# lista com os inteiros maiores que n contidos na lista
# fornecida.
# Resolução:
# 1. Adicionar n à lista através de list.append();
# 2. Ordenar a lista através de list.sort();
# 3. Pegar a fatia contendo os valores superiores a n:
# 3.1 lista indo do índice de n mais 1 até o fim;
# 4. Devolve

def maiores(listnum: list, n: int) -> list:
    '''Dada uma lista de inteiros e um inteiro n, devolve
    lista com os inteiros maiores que n contidos na lista
    fornecida'''
    list.append(listnum, n)
    list.sort(listnum)
    lista = listnum[(list.index(listnum, n) + 1) :]
    return lista