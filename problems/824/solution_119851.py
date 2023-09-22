def uppCons(frase):
    ''' Uma função que tranforma as consoantes de uma frase em letras maiuscula; str->str'''
    i=0
    cons='bcçÇdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    novaFrase = ''
    while i< len(frase):
        if frase[i] in cons:
            lm = str.upper(frase[i])
            novaFrase += lm
        else:  
            novaFrase+=frase[i]
        i += 1
	return novaFrase