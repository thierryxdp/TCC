def substitui (S,x,i):
    '''Funcao que retorna a string dada
        substituindo a posição de inteiro dada
        pelo caractere dado
        str, str, int -> str'''
    return S[0:i] + x + S[i + 1:]