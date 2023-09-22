# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    :param s: entrada de uma string
    :param x: entrada de um caractere
    :param i: entrade de um número inteiro entre 0 e a string
    :return : Retorna a string s, menos o elemento na posição i, e colocando-o pelo x"""
    
    	return s[0:i] + x + s[i + 1:]