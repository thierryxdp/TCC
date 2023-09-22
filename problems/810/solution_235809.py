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
	sp_frase=minusc.split()
	transform_lista=list(sp_frase)
	inverter=transform_lista[::-1]
    dsds=inverter.join("")
	return dsds