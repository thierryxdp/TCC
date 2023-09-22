def retira_pontuacao(s):
    """Esta função recebe uma frase e retira toda a pontuação.
    str -> str"""
	s = s.replace("."," ")
	s = s.replace(","," ")
	s = s.replace("!"," ")
	s = s.replace("?"," ")
	s = s.replace("-"," ")
	s = s.replace("_"," ")
	return s