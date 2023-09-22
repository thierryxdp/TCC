# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorna uma 
    string igual a s'''
    caracter = s[i]
    s.replace(caracter,x)
    return s