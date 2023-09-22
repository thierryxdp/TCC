# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''esta função recebe uma string s, um caractere x e um número inteiro i entre zero e o comprimento da string e retorna uma string igual a s, exceto que o elemento da posição i é substituido pelo caractere x
    string
    
    parâmetros
    s == string
    x == caractere
    i == numero inteiro
    
    
    int, int -> string'''
    return s[:i]+x+s[i+1:]