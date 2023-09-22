# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''
    	Função que substitui um caractere no elemento i de uma string s por um elemento x
		str,int,in->str    
    '''
    return s[:i] + str(x) + s[i+1:]