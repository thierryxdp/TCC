def inverte(frase):
	'''   '''
	rt_pnt=frase.replace("-"," ")
	rt_pnt=rt_pnt.replace(","," ")
	rt_pnt=rt_pnt.replace(":"," ")
	rt_pnt=rt_pnt.replace(";"," ")
	rt_pnt=rt_pnt.replace("."," ")
	rt_pnt=rt_pnt.replace("?"," ")
	rt_pnt=rt_pnt.replace("!"," ")
	minusc=rt_pnt.lower()
    sp_frase=rt_pnt.split()
	transform_lista=list(minusc)
	inverter=transform_lista[::-1]
	return inverter