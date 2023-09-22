def insere (lista_numero, n):
    for i, elemento in enumerate(lista_numero):
        if n < elemento:
            lista_numero.insert(i, n)
            return lista_numero

lista = [1,2,3,4,6,7,8,9]

n = 5

lista = insere(lista, n)

print(lista)