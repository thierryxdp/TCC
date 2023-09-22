# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao do elemento de posicao i que deve ser substituido pelo caractere x e retorne uma string igual a s;
    string,int,int -> string'''
    z=i+1
    return s[:i]+x+s[z:]