# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Recebe uma string s, um caractere x e um número inteiro I entre 0 e o comprimento da string"
    "e retorna uma string igual a s porem com o elemento da posição i substituido por x"
    if 0<=i<=(len(s)-1):
        return s[0:(i):1] + x + s[(i+1):(len(s)-1)]
    else:
        return str("Insira um número inteiro entre 0 e o comprimento da string")