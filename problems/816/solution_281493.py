def maiores(lista_numero, n):
    '''Dada uma lista de números inteiros e um número inteiro n,
      retorna outra lista, que contém todos os números da lista
      original maiores que n ordenados em ordem crescente;
      list, int -> list'''
    lista_numero.sort()
    if n>=max(lista_numero):
        return []
    elif n<min(lista_numero):
        return lista_numero
    elif n == min(lista_numero):
        return lista_numero[1:]
    else:
        def menor_ou_igual_a_n(k):
            return k<=n
        lista_numero.sort(key=menor_ou_igual_a_n)
        return lista_numero[0:lista_numero.index(max(lista_numero))+1]