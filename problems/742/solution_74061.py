# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
"""a função é definida por 's' sendo uma string 'x' algum letra a ser substituida e i um numero int que define a possição
na tupla a ser substituida. a função executa a string e escreve do ponto '0' até o ponto 'i' logo depois adicionando x que
é uma letra 

string, int, int -> string """
def substitui(s,x,i):
    return s[0:i] + x + s[i+1:]