def filtra_pares (tupla):
        '''dada um tupla com quatro elementos inteiros,
        retorna uma nova contendo apenas os números pares 
        da original e na mesma ordem;
        int, int, int, int -> int'''
        tuplaV = ()
        if tupla[0] % 2 == 0:
            tuplaV = tuplaV + (tupla[0],)
        if tupla[1] % 2 == 0:
            tuplaV = tuplaV + (tupla[1],)    
        if tupla[2] % 2 == 0:
            tuplaV = tuplaV + (tupla[2],)   
        if tupla[3] % 2 == 0:
            tuplaV = tuplaV + (tupla[3],)
            
            return tuplaV