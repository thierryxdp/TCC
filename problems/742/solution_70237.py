# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Retorna uma string igual a s com a troca do caractere de posição i pelo caractere x."
    novastr = s[:i] + x + s[i+1:]
    return novastr