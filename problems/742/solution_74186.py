# a funçao primeiro corta a primeira parte ate o indice 'i'
#depois ela adiciona a letra 'x' no meio da palavra, ai soma mais 1 com o 'i'
# e retorna o resto da palavra
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    primeira_parte = s[0:i]
    segunda_parte = s[i+1:len(s)]
    return primeira_parte + x + segunda_parte