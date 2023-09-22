# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    funcao criada para substituir a posicao de um elemento da string
    parametros:
    s: string
    x: caractere
    i: inteiro 
    saida:
    mudanca de posicao na string 
    '''
    s[i]=x
    
    return s[0:i]+x+s[i+1:]