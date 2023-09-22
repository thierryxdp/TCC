# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'dado uma string "s", um caractere "x" e um inteiro "i" retorna a string "s" , porem com o caractere "x" no lugar do caractere que estava na posição "i" '
    return s[:i] + x + s[i+1:]