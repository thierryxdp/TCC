# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que dado uma string "s" retorna a strig subtituindo algum caractere dentro dela indicado por "i" por "x".'''
    return s[:i]+x+s[i+1:]