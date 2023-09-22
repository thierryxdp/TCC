# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
	def tamanho(s):
    	if len(s)//s==0:
    		return len(s)/2
		else:
        	return len(s)/2-0.5
    return "#"+s[:tamanho(s)]+"#"+s[tamanho(s):]+"#"