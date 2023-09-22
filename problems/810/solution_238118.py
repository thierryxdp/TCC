def inverte(frase):
    """Retorna uma string sem pontuação com as mesmas palavras da strign de entrada só que com a ordem inversa;
    str->str"""
    frase=str.replace(frase,'!',' ')
	frase=str.replace(frase,'?',' ')
	frase=str.replace(frase,'.',' ')
	frase=str.replace(frase,'-',' ')
	frase=str.replace(frase,';',' ')
	frase=str.replace(frase,':',' ')
	frase=str.replace(frase,',',' ')
    frase=str.split(frase)
    frase=frase[::-1]
    return str.join(' ',frase)