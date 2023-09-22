# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dado uma string s, um caractere x e a posição de em s i, retorne s com x no lugar de outro caractere na posição i;
    string,string,int -> string'''
    S=str(s)
    A=S[i]
    S2=S.replace('A','x')
    return S2