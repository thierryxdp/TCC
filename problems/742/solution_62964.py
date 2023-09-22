# Dada uma string s, um caractere x e um número inteiro i (entre 0 e o
# comprimento de s), queremos a string com seu i-ésimo caractere
# substituído por x.
# string, string, int -> string

def substitui(s,x,i):
    '''Dada uma string s, um caractere x e um número inteiro i (entre 0 e
    o comprimento de s), devolve a string com seu i-ésimo caractere
    substituído por x. 
    Atenção: o primeiro caractere da string corresponde
    a 0, o segundo a 1 e assim por diante;
    string, string, int -> string'''
    return (a[:i] + x + a[(i+1):])