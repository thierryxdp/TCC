# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Função que recebe uma string s, um caractere x e um 
    número inteiro i que vai de 0 até o comprimento da string
    e retorna uma palavra s com o caracter x na posição i.
    str,str,int -> str'''
    return s[0:i] + x + s[i+1:]