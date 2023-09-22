# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Substitui o caractere x em razão da posição do i
    s: palavra desejada, str
    x: caractere desejado, str
    i: posição do caractere que sera substituido, int
    retorna:
    Palavra com o caractere substituido, str
    
    '''
    nova_s= s[0:i]+x+s[i+1:]
    return nova_s