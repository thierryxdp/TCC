# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Função que recebe uma string s, um caractere x
    e um número inteiro i entre 0 e o comprimento da
    string, e retorna uma string igual a s, exceto que
    o elemento da posição i deve ser substituído pelo
    caractere x.
    string, int, int -> string
    '''
    p1=s[i-2:]
    p2=s[:i-1]
    
    return p2+x+p1