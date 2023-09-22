def inverte(frase):
    '''dada uma frase(frase), retorna a mesma na ordem inversa, sem letras maiusculas e sem a pontuacao; str -> str'''
    AA = str.lower(frase)
    A = str.replace(AA, '-',' ')
    B = str.replace(A, ',',' ')
    C = str.replace(B, ':',' ')
    D = str.replace(C, ';',' ')
    E = str.replace(D, '.',' ')
    F = str.replace(E, '!',' ')
    G = str.replace(F, '?',' ')
    H = str.split(G)
    I = list.reverse(H)
    J = str.join(I)
    return J