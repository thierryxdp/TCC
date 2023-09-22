# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string e que retorna uma string igual a s porém com o elemento da posição i substituído pelo caractere x;
    str, str, int ->'''
    primeira_parte = s[0:i]
    segunda_parte = s[i+1:(len(s)]
    return primeira_parte + x + segunda_parte