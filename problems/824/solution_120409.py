def uppCons (fraseI):
	"""Calcule e retorne todas as consoantes em 
    maiúsculas e todos os caracteres da frase inicial
    (fraseI). str-->str"""
    i=0
    fraseF=""
    while i < len(fraseI):
        if fraseI[i] not in "AaEeIiOoUu" and fraseI[i]==str.upper(fraseI[i]):
        	fraseF= fraseF+faseI[i]
       	i=i+1
	return fraseF