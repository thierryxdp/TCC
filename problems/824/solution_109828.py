def maiusculaCons(frase):
    frase = frase if frase in 'AEIOUaeiouàÀáÁâÂãÃéÉêÊíÍÓóôÔúÚ' else str.upper(str(frase))
	return frase

def uppCons(frase):
    frase = list(map(maiusculaCons, frase))
    resposta = ''
    for i in range(len(frase)):
        resposta += str(frase[i])
    
    return resposta