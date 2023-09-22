# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Funcao que substitui um caracter x na posicao i na string s retornando a mesma string, exceto pelo caracter trocado na posicao i;
    	string, string, int -> string
    """
    nova_string = ""
    for char_s in s:
    	if s[i] == char_s:
            nova_string += x
            
        nova_string += char_s
        
    return nova_string