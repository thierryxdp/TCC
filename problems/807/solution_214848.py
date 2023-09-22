def conta_frase (frase):
	pontofinal = frase.replace("...", '_')
	pontodeexclamcao=pontofinal.replace("!",'_')
	pontodeinterrogacao=pontodeexclamacao.replace("?",'_')
	reticencias=pontodeinterrogacao.replace(".",'_')
	return reticencias.count('_')