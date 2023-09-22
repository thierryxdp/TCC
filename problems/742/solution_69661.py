# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    Função que recebe, respectivamente uma string "s" 
    um caractere x, e um numero inteiro i entre 0 e 
    o comprimento da string e retorna uma string igual a 
    s, exceto que o elemnto da posição i deve ser substituido
    pelo caractere x
    '''
    y=i-1
    return s[0:y]+"x"+s[i:]