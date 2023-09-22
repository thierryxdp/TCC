# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    # uma função que rece uma string, um caractere e um numero inteiro entre
    #0 e o comprimento da string e retorna uma string igual a s, exceto que
    #o elemento da posiçao i deve ser substituido pelo caractere x
    # str, int, int > str
    return s[:i] + x + s[i-1:]