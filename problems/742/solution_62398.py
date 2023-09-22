# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    string = s
    '''função que recebe uma string (s), um caracter (x) e um numero inteiro (i),
e retorna a string s, atribuindo i a um termo da string e substituindo-o por x'''
    return string[0:i]+x+string[i+1:]