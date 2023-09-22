# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma string, um caracter e um
    inteiro e retorna uma string, substintuindo na string s
    um caracter x na posicao i, dado o valor de um inteiro 
    entra 0 e o comprimeiro da string
    entrada: string, int, int 
    saida: string
    '''
    comprimentoStr= 0<i<len(str(s))
    susbstituindo= s[0:(i-1)]
    resto= s[(i+1):]
    return susbstituindo+str(x)+resto