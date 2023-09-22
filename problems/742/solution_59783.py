# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que,ao receber uma string s, um caractere x e um número inteiro i, retorne uma string igual a s, exceto que o elemento da posiçao i deve ser substituído pelo caractere x; str,str,int -> str'''
    subst=len(s)//2
    return s[0:i] + x + s[i+1:len(s)]