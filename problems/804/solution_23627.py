def filtra_pares(t):
        '''recebe uma tupla com 4 valores inteiros e retorna uma tupla somente com os valores pares na mesma ordem em que se encontravam
        tup->tup'''
        pares=()
        
        if (t[0])%2==0:
            pares=pares + (t[0],)
        if (t[1])%2==0:
            pares=pares + (t[1],)
        if (t[2])%2==0:
            pares=pares + (t[2],)
        if (t[3])%2==0:
            pares=pares + (t[3],)
        else:
            return pares