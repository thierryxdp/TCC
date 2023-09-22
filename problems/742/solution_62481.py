# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    substitui o último caracter de uma strig por x
    parâmetros
    	s,x,i:str,str,int
    saída
    	sttr
    '''
    i = len(s)
    s_copy = s[0:i-1]+x
    return s_copy