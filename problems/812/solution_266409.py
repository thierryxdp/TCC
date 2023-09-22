def retira_pontuacao(frase):
	"""Calcula e retorna uma nova frase, trocando os 
caracteres de pontuacao(travessao,virgula,dois pontos,
ponto e virgula,ponto,ponto de exclamacao, ponto de
interrogacao e tres pontos)da variavel de entrada "frase"
por espacos; str --> str"""
    y=frase.replace("-","")
    x=y.replace("!","")
    z=x.replace(";","")
    p=z.replace(",","")
    q=p.replace(".","")
    r=q.replace(":","")
    s=r.replace("?","")
	t=s.replace("!","")
    return t