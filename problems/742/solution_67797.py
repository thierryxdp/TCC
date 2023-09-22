# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e o 
    número inteiro i entre 0 e o comprimento da string e 
    retorna uma string igual a s substituindo o elemento
    da posição i pelo caractere x'''
    return s[0:i] + x + s[i+1:]