# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Substitui e retorna uma string s com a posição i alterada com o valor x
        str, int, int -> str'''
    
    s[i] = x
    
    return s