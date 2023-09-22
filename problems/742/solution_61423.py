def substitui (S,x,i):
    S[i] = str(x)
    '''Funcao que retorna a string dada
        substituindo a posição de inteiro dada
        pelo caractere dado
        string, int, int -> string'''
    return S[0:i] + x + S[i + 1:]