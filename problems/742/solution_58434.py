# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """dada uma string s, um caractere x e um número inteiro i entre 
0 e o comprimento da string, a função retorna uma string igual a s, 
mas substituindo o caractere da posição i por x.
string, string, int --> string"""
    return s[0:i]+str(x)+s[i+1:-1]+s[-1]