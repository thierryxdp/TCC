# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui oum caractere da string (s) pelo caractere (x) na posição (i) (str,str,int->str)'''
    s[i]=str(x)
    return s