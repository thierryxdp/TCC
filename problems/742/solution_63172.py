# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Escreva uma string(s), um caractere(x) e um número inteiro(i) entre 0 e o comprimento da string e o valor retornado será s modificado por x na posição i'''
    sl=list(s)
    sl[i]= x
    s="".join(sl)
    return s