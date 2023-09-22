# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dada uma string s, um caractere x e um número inteiro i,
    retorna uma string igual a s, porém com x substituindo a posição
    do número inteiro i;
    string,string,int->string"""
    y=len(s)
    return s[0:i]+x+s[i:y]