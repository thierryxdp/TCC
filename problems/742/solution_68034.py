# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string(s) com o elemento da posição(i) substituido pelo elemento da posição(x). [entrada ->(str,int,int)] [saida->(str)]'''
    s[i] = x
    return s