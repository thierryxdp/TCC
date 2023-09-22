# Dada uma lista de números inteiros e um número inteiro n,
# retorna a lista com o n e ordenada crescentemente
# list, int -> list
def insere(lista_numero, n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero