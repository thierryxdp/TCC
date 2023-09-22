# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui uma letra dentro de uma palavra"""
    efeito=s[:i]+x+s[i+1:]
	return efeito