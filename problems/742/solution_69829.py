# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''substitui a letra (x) na posição(i) escolhida'''
    
    metade1 = s[0:i]
    metade2 = s[i+1:len(s)]
    
    return metade1 + x + metade2