# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'Funcao que, dado uma string s, um caraceter x e um numero inteiro i entre 0 e o comprimento da string, retorna uma string igual a s, exceto que o elemento da posicao i deve ser substituido pelo caractere x.'
    'Entrada: str, int, int'
    'Saida: str'
    return s[0:i] + x + s[i+1:]