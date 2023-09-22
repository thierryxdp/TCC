# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Ex:
    A M A N D A 
    0 1 2 3 4 5
    len(Amanda)= 6
    '''
    if i==0:
        return x+s[1:]
    
    elif i>0:
        return s[0:i] + x + s[i + 1:]
    
    else:
        return s[len(s)] +x