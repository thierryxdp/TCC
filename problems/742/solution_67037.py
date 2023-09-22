# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que substitui um caractere da str pelo x;str,str,int->str '''
    parte1=s[:i]
    parte2=s[i+1:]
    return parte1+x+parte2