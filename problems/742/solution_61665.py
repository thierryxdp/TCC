# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' funcao que recebe uma string s, um caracter x e um numero i, com o comprimento entre 
    0 e a string 
    str, char, int -> '''
    if 0<=i<=(len(s)-1):
        return s[:i]+x+s[i+1:]