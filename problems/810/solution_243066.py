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
def inverte(texto):
    """inverte a ordem das palavras de um texto(de tras pra frente)
    retrando a pontuacao e letras maiusculas.
    entra texto;str->str"""
    texto=str.lower(texto)
    texto=retira_pontuacao(texto)
    texto=texto[len(texto)-1:0:-1]+texto[0]
    return texto