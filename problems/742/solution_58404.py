# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string (s), um caractere (x) e um número inteiro (i)
    que deve ser menor que o comprimento da string e retorna uma modificação da 
    string (s) com o caractere (x) na posição (i); int, int -> string'''
    
    inicioString = s[:i]
    fimString = s[i+1:]
    return inicioString+x+fimString