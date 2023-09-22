# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(str(s),x,i):
    '''calcula string que substituia o caractere de posição i por x
    str,int,int->str'''
    
    str(s)[i] = x
    
    return s[0:i] + x + s[(i+1):]