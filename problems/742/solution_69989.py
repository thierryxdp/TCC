# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna a string = a str, com o elemento "i" sendo substituido por x'''
    '''str,str,int --> str'''
    
    return s[0:i] + x + s[i + 1:]