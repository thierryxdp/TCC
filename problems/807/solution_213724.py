def conta_frases(frases):
	''' '''
	import re
    sp_frases=re.split(". |! |? |...", frases)
	lista_frases=list(sp_frases)
	qnt_frases=len(lista_frases)
	return qnt_frases