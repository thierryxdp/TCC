def uppCons(frase):
    '''Função que pega a frase de entrada e retorna a frase com as consoantes em maiúsculo
    	str, str→str'''
    indice=0
	while indice < len(frase):
    	if frase[indice] in 'bcçdfghjklmnpqrstvwxyz':
    		maiuscula = str.upper(frase[indice])
        	frase=frase.replace(frase[indice],maiuscula) 
        indice+=1
    return frase