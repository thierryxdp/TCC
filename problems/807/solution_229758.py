def conta_frases (frase):
    ''' retorna a quantidade de frases que aparecem no texto;
    entrada é a frase; str ->str'''
	frase1= str.replace(frase,'!','x')
    frase2= str.replace(frase1,'?','x')
    frase3= str.replace(frase2,'.','x')
    frase4= str.replace(frase3,'xxx','x') 
    contou= str.count(frase3,'x')
    return contou