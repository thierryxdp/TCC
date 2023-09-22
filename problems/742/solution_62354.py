# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao que dado string s,caractere x e int i retorna s com modificacao
    na posicao i
    	Parametros:
        s,x,i: str,int
        Saida:
		str'''
    return s[0:i-1]+ x+ s[i+1:]