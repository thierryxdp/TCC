# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe uma string, uma letra e sua posição e 
    susbtitui a letra nessa mesma posição'''
    return s[:i]+ x+s[i+1:]