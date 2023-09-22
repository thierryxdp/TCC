# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s, x, i):
    '''Recebe uma string 's', um caractere 'x' e um número inteiro 'i' entre
    0 e o comprimento da string e retorna uma string igual a s, trocando o
    elemento da posição 'i' pelo caractere 'x'.
    str, (str ou int) ,int -> str'''
    
    posicao_i = s[i]
    primeiraParte = s[:i]
    segundaParte = s[i+1:]

    return primeiraParte + str(x) + segundaParte