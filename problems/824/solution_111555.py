def uppCons(f):
	vogais = "AEIOUaeiou"
	r = ""
	for i in range(len(f)):
		if f[i] not in vogais:
			r = r + f[i].upper()
		else:
			r = r + f[i]
	return r