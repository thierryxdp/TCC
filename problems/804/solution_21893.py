def filtra_pares (tupla):
    '''função que dados quatro elentos inteiros retorne quais deles são pares
     na mesma ordem em que já haviam sido informados.
     int, int, int, int -> tuple'''
    saida=()
    if tupla[0]%2==0:
        saida+=(tupla[0],)
    if tupla[1]%2==0:
        saida+=(tupla[1],)
    if tupla[2]%2==0:
        saida+=(tupla[2],)
    if tupla[3]%2==0:
        saida+=(tupla[3],)
    return saida