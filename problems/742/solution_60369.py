# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ retorna a string fornecida com a troca de um elemento na posiçao desejada
    parameters:
    s: string
    x: novo caracter
    i: posiçao do elemento a ser substituido
    returns:  nova string com elemento substituido"""
    return s[ :1] + x + s[i+1:]