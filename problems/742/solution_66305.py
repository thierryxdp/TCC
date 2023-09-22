# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caracter e um número inteiro i(0<i<comprimento da string) dados como entrada
    e retorna a string s exceto que o elemento da posição i é substituído pelo caracter
    str,int,int->str'''
    return s[0:i]+x+s[i+1:]