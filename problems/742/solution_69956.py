# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna uma string igual a , exceto com caracter substituido, dado sua sting, caractere e posição'''
   
a = s[0:i]
    b = s[i+1:len(s)]
    return a+x+b