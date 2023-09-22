# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retona uma string igual a s exceto que  elemento da posição i (nímero interiro)
    deve ser substituído pelo caractere x
    str,str,int->str'''
    return s[:i]+"x"+s[(i+1):]