# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(x,i,s='s'):
    '''Dado uma string s, substitua o caractere x por um dos caracetres de s na posição i;
    string,int,int -> string'''
    S=str(s)
    S2=S[0:i]+'x'+S[i+1:]
    return S2