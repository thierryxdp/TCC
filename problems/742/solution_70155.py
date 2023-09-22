# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  	"""substitui em s um caracter x na posição i,substitui(s,x,i)"""
	# 0<i<ilen(s)
    return s[0:i] + str(x) + s[i+1:int(len(s))]