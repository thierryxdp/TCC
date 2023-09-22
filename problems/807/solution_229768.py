def conta_frases (frase):
    ''' retorna a quantidade de frases que aparecem no texto;
    entrada é a frase; str ->str'''
	frase2= str.replace(frase,'!','x')
    frase3= str.replace(frase2,'?','x')
    #frase3= str.replace(frase2,'.','x')
    frase4= str.replace(frase3,'. ','x') 
    frase5= str.replace(frase4,'... ','x')
    frase6= str.replace(frase5,'...','x') 
    contou= str.count(frase6,'x')
    return contou