def fatorial(n):
        '''Dado um número a função retorna o fatorial do mesmo
           int -> int
           Parametros:
           n : número escolhido'''
        fatorial = 1
        i = 2
        while i <= n:
                fatorial = fatorial * i
                i += 1
        return fatorial