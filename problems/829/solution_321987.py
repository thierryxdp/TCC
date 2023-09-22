def h(n):

        return 1/n


def soma_h(n):

        lista = [i for i in range(1, n+1)]

        lista = map(h, lista)

        saida = 0

        for i in lista:

                saida += i

        return round(saida, 2)