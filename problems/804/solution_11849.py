def filtra_pares(e1,e2,e3,e4):
    '''Funcao que, dados quatro inteiros, retorna uma nova tupla contendo os elementos pares da tupla inicial na mesma ordem em que se encontravam; recebe uma tupla de entrada e retorna uma tupla'''
    pares=()
    (e1,e2,e3,e4)=elementos
    if elementos[0]%2==0:
        pares=(pares+elementos[0])
    if elementos[1]%2==0:
        pares=(pares+elementos[1])
    if elementos[2]%2==0:
        pares=(pares+elementos[2])
    if elementos[3]%2==0:
        pares=(pares+elementos[3])
        return pares