# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """dado uma string s, um caractere x e um número inteiro i,
    a função retorna uma string igual a s, com o elemento da posição i
    substituido pelo caractere x;
    str,str,int->str"""
    A=s[:i]
    B=s[i+1:]
    return A+x+B