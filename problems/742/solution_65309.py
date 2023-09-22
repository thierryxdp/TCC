# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''ao receber uma string s, um caractere x e um
    número inteiro i entre 0 e o comprimento da string,
    retornará uma string onde o elemento da posição i
    é substituído pelo caractere x.
    str, str, -> str'''
    if i == 0:
        return x + s[1:]
    elif i == len(s):
        return s[0:len(s)]
    else:
        return s[0:i] + x + s[i+1:]