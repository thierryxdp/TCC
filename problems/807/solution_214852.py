def conta_frases (frases):
	pontofinal = frases.replace("...", '_')
	pontodeexclamcao = pontofinal.replace("!",'_')
	pontodeinterrogacao = pontodeexclamacao.replace("?",'_')
	reticencias = pontodeinterrogacao.replace(".",'_')
	return reticencias.count('_')