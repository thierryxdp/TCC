# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Recebe uma string s, e substitui um caractere da posição i
    pelo caractere x.
    string,string,int -> string'''
    
    string1 = s[:i]
    string2 = s[i+1:]
    
    return string1 + x + string2