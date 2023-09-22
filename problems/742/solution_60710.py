# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
'''Dado como parametro uma string s, um caracter x, e um numero inteiro i entre zero e o comprimento
da string que retorne uma string igual a s, exceto o elemento da posicao i, que deve ser
substituido pelo caractere x.
   str,str,int -> str'''
    return s[0:i] + str(x) + s[i+1:]