# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    '''
    
       str, int, int -> str
       str(i)=x
    '''
    a=s[0:1]+str(x)+s[i+1:]
    return a