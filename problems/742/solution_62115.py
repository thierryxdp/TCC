# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    funcao criada para formar uma string em que a posicao dos parametros i deve ser substituida
    pelo caractere x 
    parametros:
    s: string
    x: caractere
    i: numero inteiro 
    saida: 
    string 
    '''
    s(i)=x
    
    return s[0:i]+x+s[i+1:]