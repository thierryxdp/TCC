# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string s, um caractere qualquer x e um número inteiro i
   . Retorna a string s mas com o caractere x substituído na posição i; str,
   int, int -> string'''
    return s[0:i]+x+s[i+1:]