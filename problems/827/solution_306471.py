def qtd_divisores(n):

        divisores = lambda t: n%t == 0 

        lista = [i for i in range(1, n+1)]

        lista = list(filter(divisores, lista))

        return len(lista)