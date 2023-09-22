# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que faz substituição.
    string, int, int -> string'''
    
    antes_de_x = s[0:i]
    depois_de_x = s[i+1:len(s)]
    
    return antes_de_x + x + depois_de_x