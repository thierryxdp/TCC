# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    	Função que retorna a string s modificada na posição i pelo caractere x
        str,int,int -> str
    '''
    return s[0:i] + str(x) + s[i:-1]