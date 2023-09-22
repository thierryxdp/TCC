'''Recebe uma lista de numeros e um numero n, e retorna outra lista contendo os elementos da lista original multiplos de n'''
#list, int -> list

filtraMultiplos(lista, numero):
    lista2 = []
    contador = 0
    while contador < len(lista):
        if lista[contador] % numero == 0:
            lista2 = lista2 + [lista[contador]]
        contador = contador + 1
    return lista2