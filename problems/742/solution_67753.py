# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Essa funcao recebe como entrada uma string e retorna a mesma com o elemento da posicao i substituido pelo caractere x
    str->str'''
    def substitui(s, x, i):
    s[i] = x
    return s
   # return s[0:i] + x + s[i + 1:]