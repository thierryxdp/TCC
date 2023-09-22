def conta_frases (frase):
	pontofinal = frase.replace("...", '_')
	pontodeexclamcao=pontofinal.replace("!",'_')
	pontodeinterrogacao=pontodeexclamacao.replace("?",'_')
	reticencias=pontodeinterrogacao.replace(".",'_')
	return reticencias.count('_')