# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' Função que substitui um caractere numa string definida pelo usuário 
    		Parâmetros:s = string original
            			x = caractére definido pelo usuário
                        i = índice definido pelo usuário
                        string, string, int -> string '''
 	return s[0:i] + str(x) + s[i +1:]