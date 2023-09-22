# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''''funcao receve uma string retorna uma string igual a s e i substitui x''''
    aux = s[0:i] + x + s[i+1:len(s)]
    return aux