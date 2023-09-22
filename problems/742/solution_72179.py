# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ""retorne uma string igual a s exceto que o elemento da posicao i deve ser substituido pelo caractere""
    return s[0:i] + x + s[i+1:]