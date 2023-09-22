# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Funcao que substitui um caracter x na posicao i na string s retornando a mesma string, exceto pelo caracter trocado na posicao i;
    	string, string, int -> string
    """      
    return s[0:i] + x + s[i + 1:len(s)]