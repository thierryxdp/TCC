# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string s, um caractere x e um numero inteiro i e 
    retorna ums string igual a s porem o elemento da posição i deve ser substituido pelo caractere x
    string, int, int -> string'''
    
    subs1=s[0:i]
    subs2=s[(i+1):]
    return str(subs1)+str(x)+str(subs2)