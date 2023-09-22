# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
  '''
  
  '''
	if i=0:
        return 'x' + s[1:]

	if i=len(s):
        return s[:-2] + 'x'


	if i>0 and i<len[s]:
        return s[:i] + 'x' + s[i+1:len(s)]