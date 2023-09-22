# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que, dada uma string s, um caractere x e um número inteiro i, entre 0 e o comprimento da string, retorna uma string igual a s, exceto que o elemento da posição i deve ser substituido pelo caractere x; str,str,int->str"""
    A = s[0:i]+x
    if s[i]==s[-1] and (i+1) != len(s):
        return A+s[(i+1):-1]+s[-1]
    elif s[i]==s[-1]:
        return A
    elif not s[i]==s[-1]:
        return A+s[(i+1):-1]+s[-1]