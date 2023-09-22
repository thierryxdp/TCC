def classificacao(cv, ce, cs, fv, fe, fs):
	"""
    informar vitorias, empates e gols de cada time
    """
	#ptc = pontos totais cormengo
	#ptf = pontos totais flaminthians
	ptc = 3*cv + ce
	ptf = 3*fv + fe
	if (ptc == ptf):
		if (cs > fs):
			return 'Cormengo'
		elif (cs < fs):
			return 'Flaminthians'
		else:
			return 'Empate'
	elif (ptc > ptf):
		return 'Cormengo'
	else:
		return 'Flaminthians'