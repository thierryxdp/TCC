def soma_h(N):
        '''Dado um número N, a função deve calcular e retornar
        o valor de H com N termos;
        int->float'''
        H=0
        for i in (1,N+1):
            x=1/i
            H=H+(x)
            
        return(round(H,2))