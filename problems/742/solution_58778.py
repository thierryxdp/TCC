# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao recebe uma string s, um caractere x e um numero inteiro i entre
0 e o comprimento da string e retorna um strig igual a s, exceto que o elemento
da posicao i deve ser substituido pelo caractere x.
    Parametro de entrada: string, string, int
    Valor de retorno: string'''
    s = s[:i]+x+s[i+1:]
    return s