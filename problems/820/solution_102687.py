def posLetra(string,letra,n):
    '''funcao que recebe uma frase em string, uma letra e um numero
       e retorna a posicao que essa letra aparece na frase, caso
       o numero que indica a posicao desejada seja maior que a 
       ocorrencias de letras, retorna -1.
       str, str, int -> int'''
    i = 0
    novo = string
    if n > string.count(letra):
        return -1
    while i < n:
        x= str.index(novo,letra)
        novo= novo[x:]
        i += 1
    return len(string) - len(novo)