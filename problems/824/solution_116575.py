def uppCons(passe):
	"""
"""
	fim=()
	cont=0
	while cont<len(passe):
		if passe[cont]!='AEIOUaeiou':
			fim= fim+(str.upper(passe[cont]))
		cont=cont+1
	return fim