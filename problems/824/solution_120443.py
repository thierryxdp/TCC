def uppCons (fraseI):
	"""Calcule e retorne todas as consoantes em 
    maiúsculas e todos os caracteres da frase inicial
    (fraseI). str-->str"""
	i=0
	fraseF= fraseI
	while i < len(fraseI):
    	if fraseI[i] not in "AaEeIiOoUuÃãÍíÚúÉéÀàÁáÓó":
   		fraseF= fraseF.replace(fraseF[i],(str.upper(fraseF[i])),i)
        i=i+1
	return fraseF