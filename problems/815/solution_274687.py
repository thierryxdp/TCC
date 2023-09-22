def insere(lista_numero, n):
    """Dada uma lista de números inteiros
que seja ordenada em ordem crescente e um número inteiro <n>, retorna a
lista com o número inteiro <n> na posição correta, ou seja, fazendo com que
a lista continue ordenada em ordem crescente.
assinatura: list, int --> list
casos de teste:
insere([1, 2, 17, 19], 10) == [1, 2, 10, 17, 19]
insere([1, 2, 4, 5, 6], 3) == [1, 2, 3, 4, 5, 6]
insere([100, 200, 300], -100) == [-100, 100, 200, 300]
insere([-100, -200, 100, 200], -150) == [-200, -150, -100, 100, 200]
"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero