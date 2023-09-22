def inverte(frase):
	'''   '''
	rt_pnt=frase.replace("-"," ")
	rt_pnt=rt_pnt.replace(","," ")
	rt_pnt=rt_pnt.replace(":"," ")
	rt_pnt=rt_pnt.replace(";"," ")
	rt_pnt=rt_pnt.replace("."," ")
	rt_pnt=rt_pnt.replace("?"," ")
	rt_pnt=rt_pnt.replace("!"," ")
	sp_frase=rt_pnt.split()
	minusc=sp_frases.lower()
	transform_lista=list(minusc)
	inverter=transform_lista[::-1]
	return inverter