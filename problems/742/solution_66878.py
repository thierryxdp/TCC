# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ essa função recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento
da string, e retorna uma string igual a s, exceto que o elemento da posição i é substituído pelo
caractere x.
str,str,int -> str"""
    if len(s)>= i >=0 :
        return s[0:i] + x + s[i+1:]