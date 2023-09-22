def filtra_pares(elementos):
    '''Funcao que, dados quatro inteiros, retorna uma nova tupla contendo os elementos pares da tupla inicial na mesma ordem em que se encontravam; recebe uma tupla de entrada e retorna uma tupla'''
    pares=()
    (e1,e2,e3,e4)=elementos
    if int (elementos[0])%2==0:
        pares=pares+(elementos[0],)
    if int (elementos[1])%2==0:
        pares=pares+(elementos[1],)
    if int (elementos[2])%2==0:
        pares=pares+(elementos[2],)
    if int (elementos[3])%2==0:
        pares=pares+(elementos[3],)
    return pares