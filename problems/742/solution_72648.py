# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dada uma string s, um caractere x e um número i entre 0 e o tamanho da string. E substitui x pelo na posição i
    str,str,int -> str'''
    return s[0:i] + x + s[i+1:]