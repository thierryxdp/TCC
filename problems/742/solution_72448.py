# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe uma string e retorna alterando
    caractere número i por x
    str str int --> str'''
    palavra_nova = s[:i] + x + s[i+1:]
    return palavra_nova