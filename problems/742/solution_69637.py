# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
        A função recebe uma string, x e um número inteiro e
        retorna a string dada com o caractere x no lugar 
        correspondente ao inteiro (i)
        str, int, int -> str
    '''
    s[i] = 'x'
    return s[0:i] + s[i] + s[i+1]