def soma_h(N):
        '''funcao que calcula o valor da soma h com N termos; int -> int'''
        valorH = 0
        for N in range(N + 1):
            if N > 0:
                valorH = valorH + 1/N
            return round(valorH,2)