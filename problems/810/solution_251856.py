def inverte (frase):
	"""Calcula e retorna a variavel de entrada"frase"
na sua forma inversa, sem letras maiusculas e pontuacao;
str-->str"""
    y=frase.replace("-","")
    x=y.replace("!","")
    z=x.replace(";","")
    p=z.replace(",","")
    q=p.replace(".","")
    r=q.replace(":","")
    s=r.replace("?","")
    t=s.replace("!","")
    a=t.lower
    return