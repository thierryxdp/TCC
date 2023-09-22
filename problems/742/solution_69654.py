# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
        Função que recebe s (string), x (caractere) e 
        i (número inteiro) e retorna a string informada com 
        o x na posição do número inteiro informado
        str, int, int -> str
    '''
    0 <= i <= len(s)
    s[i] == x
    return s[0:i] + x + s[i+1:]