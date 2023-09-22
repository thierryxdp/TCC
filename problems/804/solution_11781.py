def filtra_pares(tupla):
        '''Recebe uma tupla de quatro elementos inteiros e devolve
           uma nova tupla contendo apenas os elementos inteiros pares.
           tuple(int, int, int, int) -> tuple(int, int, int, int)'''
        tupla_final = ()
        if int(tupla[0])%2 == 0:
            tupla_final = tupla_final + (tupla[0],)
        if int(tupla[1])%2 == 0:
            tupla_final = tupla_final + (tupla[1],)
        if int(tupla[2])%2 == 0:
            tupla_final = tupla_final + (tupla[2],)
        if int(tupla[3])%2 == 0:
            tupla_final = tupla_final + (tupla[3],)
        return tupla_final#Start your python function here