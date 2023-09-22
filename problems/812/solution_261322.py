def retira_pontuacao(texto):
	"""substitui qualquer pontuacao por espaço.
entra texto; str->str"""
	texto=str.replace(texto,'...',' ')
	texto=str.replace(texto,'!',' ')
	texto=str.replace(texto,'.',' ')
	texto=str.replace(texto,'?',' ')
	texto=str.replace(texto,';',' ')
	texto=str.replace(texto,':',' ')
	texto=str.replace(texto,'-',' ')
	texto=str.replace(texto,',',' ')
	return texto