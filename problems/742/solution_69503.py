# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    função que recebe uma string (s), um caractere (x) e um numero inteiro (i). A função irá retornar
    uma string s, com o elemento da posição i substituio pelo caractere x.
    string, int, int -> string
    '''
    if i==0:
        return x+s[1:]
    
    elif i>0:
        return s[0:i] + x + s[i + 1:]
    
    else:
        return s[len(s)] +x