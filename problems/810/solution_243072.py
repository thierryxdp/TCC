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
    """deixa um texto de tras pra frente sem pontuacao e
    sem letra maiuscula. entra texto;str->str"""
    texto=str.lower(texto)
    texto=retira_pontuacao(texto)
    texto=str.split(texto)[len(str.split(texto))-1:0:-1]+[str.split(texto)[0]]
    texto=str.join(' ',texto)
    return texto