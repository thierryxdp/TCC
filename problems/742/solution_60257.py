# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que dada uma string s, um caracter x e um número inteiro i entre 0 e o comprimento da string,retorna uma string igual a s,
    exceto que o elemento da posição i deve ser substituído pelo caractere x'''
    return s[0:i] + x + s[i+1:]