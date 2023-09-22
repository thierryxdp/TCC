def filtra_pares(tupla):
    "funçao que recebe quatro parametros inteiros em forma de tupla e retorna uma nova tupla apenas com os valores pares da original" 
    tuplaN=()
     if tupla[0] % 2 == 0:
            tuplaN = tuplaN + (tupla[0],)
        if tupla[1] % 2 == 0:
            tuplaN = tuplaN + (tupla[1],)
        if tupla[2] % 2 == 0:
            tuplaN = tuplaN + (tupla[2],)
        if tupla[3] % 2 == 0:
            tuplaN = tuplaN + (tupla[3],)
        return tuplaN
        



#Start your python function here