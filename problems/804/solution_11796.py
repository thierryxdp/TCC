def filtra_pares(e1,e2,e3,e4):
    '''Funcao que, dados quatro inteiros, retorna uma nova tupla contendo os elementos pares da tupla inicial na mesma ordem em que se encontravam; recebe uma tupla de entrada e retorna uma tupla'''
    pares=()
    if e1%2==0:
        pares=(pares+str(e1))
    if e2%2==0:
        pares=(pares+str(e2))
    if e3%2==0:
        pares=(pares+str(e3))
    if e4%2==0:
        pares=(pares+str(e4))
        return pares