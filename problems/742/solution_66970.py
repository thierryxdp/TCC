# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Função que substitui uma caractere em uma frase na posição indicada.
    Dado a frase, o novo caractere, e a posição para substituição.
    str,str,int->str'''
    return s[0:i] + x + s[i + 1:]