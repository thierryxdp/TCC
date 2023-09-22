def classificacao(cv, ce, cs, fv, fe, fs):

	ptc = 3*cv + ce
	ptf = 3*fv + fe
    
	if (ptc == ptf):
		if (cs > fs):
			return ’Cormengo’
		elif (cs < fs):
			return ’Flaminthians’
		else:
			return ’Empate’
        
	elif (ptc > ptf):
		return ’Cormengo’
	else:
		return ’Flaminthians’