def posLetra(frase, L, n):
    '''
    Funçao que recebe uma frase, letra e numero e retorna 
    o indice da letra em relaçao ao numero
    str, str, int -> int
    '''
    x=str.find(frase,L)
    while x >= 0 and n > 1:
        x = str.find(frase, L, x+1)
        n = n+1
    return x