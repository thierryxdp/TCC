# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "retoorna uma string igua a s exceto que o elemento da posiçao i deve ser substiuido por x"
    return str(s)[0:i] + x + str(s)[i + 1:]