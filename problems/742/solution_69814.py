# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string igual a 's', porém com o caractere 'x' substituindo o caractere da posição i
    	str, str, int -> str'''
    return s[:i] + x + s[i+1:]