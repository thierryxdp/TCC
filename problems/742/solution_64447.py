# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma string s, um caractere x
    e um numero inteiro i entre o comprimento da string,
    e retorne uma string igual a s, exceto o elemento 
    da posicao i, ele sera subistituido pelo caractere x
    string,string,int->string'''
    return s[0:i] + x + s[i+1:len(s)]