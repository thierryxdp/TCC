def conta_frases (frase):
	pontofinal = frase.replace("....", '_')
	pontodeexclamcao=pontofinal.replace("!",'_')
	pontodeinterrogacao=pontodeexclamacao.replace("?",'_')
	reticencias= pontointerrogacao.replace(".",'_')
	return reticencias.count('_')