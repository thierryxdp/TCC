def retira_pontuacao(frase):
	'''Função que retorna a frase sem os caracteres de pontuação
    str->str'''
	rt_pnt=frase.replace("-"," ")
	rt_pnt=rt_pnt.replace(","," ")
	rt_pnt=rt_pnt.replace(":"," ")
	rt_pnt=rt_pnt.replace(";"," ")
	rt_pnt=rt_pnt.replace("."," ")
	rt_pnt=rt_pnt.replace("?"," ")
	rt_pnt=rt_pnt.replace("!"," ")
	return rt_pnt