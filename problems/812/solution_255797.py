def retira_pontuacao(frase):
	''' '''
	rt_pnt=frase.replace("-"," ")
	rt_pnt=rt_pnt.replace(","," ")
	rt_pnt=rt_pnt.replace(":"," ")
    rt_pnt=rt_pnt.replace(";"," ")
    rt_pnt=rt_pnt.replace("."," ")
	return rt_pnt