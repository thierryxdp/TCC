def conta_numero(numero,matriz):
    """'Determina quantas ocorrencias um elemento tem na lista;int,list=>int"""
	#ultilei essa formatacao pois as lihas escritas seria curtar demais.
    contador = sum(i.count(numero) for i in matriz)
	return (contador)