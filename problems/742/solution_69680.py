# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dados os valores da string s, do caractere x e do número inteiro i entre 0 e o comprimento da string,
    retorna uma string igual a s, exceto pelo elemento da posição i que deve ser substituido por x'''
    return str(s[:i])+str(x)+str(s[i:])