# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    funcao que recebe string s, um caracter x e um numero i
    e retorna uma string s e na posicao i substitui pelo caracter x
	param: 
    string - s
    caracter x - string
    numero inteiro - i
    retorna - string
    '''
    
    
    return s[:i] + 'x' + s[i+1:]