# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Esta função substitui um caractere escolhido na string dada'''
    k = s[0:i] + str(x)
    j = s[i:-1]
    return str(k)+str(j)