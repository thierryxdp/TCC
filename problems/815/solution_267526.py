"""Recebe uma lista de numeros em ordem crescente e um inteiro. Retorna uma nova
lista com o inteiro inserido na posição ordenada certa.
list, int -> list"""
def insere(lista_numero, n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero