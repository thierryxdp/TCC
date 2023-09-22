# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  	"""str,int,int -> str; Função que substitui caracteres de uma string."""
 	x=int(len(s))
    if s[7]==x:
        return s[0:6]+'x'