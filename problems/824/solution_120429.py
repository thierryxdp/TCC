def uppCons (fraseI):
	"""Calcule e retorne todas as consoantes em 
    maiúsculas e todos os caracteres da frase inicial
    (fraseI). str-->str"""
	i=0
	fraseF=""
	while i < len(fraseI):
    	if fraseI[i] not in "AaEeIiOoUu":
   		fraseF= fraseF + str.replace(fraseI,fraseI[i],(str.upper(fraseI[i])))
        i=i+1
	return fraseF