# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Função que recebe uma string, um caractere e uma posição, e retorna a string s com o caractere x na posição i 
    
    string, string, int -> string
    '''
    return s[:i]+str(x)+s[i+1:]