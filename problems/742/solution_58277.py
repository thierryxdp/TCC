# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(x,i,s='s'):
    '''Dado uma string s, substitua o caractere x por um dos caracetres de s na posição i;
    string,string,int -> string'''
    S=str(s)
    X=str(x)
    S2=S[0:i]+X+S[i:]
    return S2