def soma_h(N):
        '''Dado um número N, a função deve calcular e retornar
        o valor de H com N termos;
        int->float'''
        H=0
        for i in range(1,N+1):
            H=H+(1/i)
            
        return(round(H,2))