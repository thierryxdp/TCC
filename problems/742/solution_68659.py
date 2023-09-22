# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    	Funcao que recebe uma string(s), um caractere (x) e 
        um numero inteiro (i) entre 0 e o comprimento da 
        string, e retorna uma string igual a s
        string, int, int -> string
    '''
    y = s[0:i] + s[i] + s[i+1:]
    return y