# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Substitui um caractere na posição I de uma string S pelo caractere X
       Entrada: str, int, int
       Saída: str
       """
	o = i
    p = o + 1
    return s[:o]+"x"+s[p:]