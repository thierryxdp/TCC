# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao que recebe uma string e um caractere no comprimento da string escolhida pelo usuario e retorna o caractere
    	Parametro: s = string original
        			x = caractere escolhido
                    i = indice escolhido
                    	str, str, int -> str '''
    
    	return s[0:i] + str(x) + s[i+1:]