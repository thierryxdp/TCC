# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento 
    da string, retorna uma string igual a s, mudando a posicao i pelo elemento x'''
    
    s[i] = x 
    return s