# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
	"""
    Essa funcao substitui um caractere por outro em determinada posicao
    Parametros: s,x,i(string, int, string)
    saida: string
    """
    r = s[0:i] + x + s[i+1:]
    return r