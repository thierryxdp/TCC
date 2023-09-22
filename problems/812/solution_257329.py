def retira_pontuacao(s):
	s = s.replace("."," ")
	s = s.replace(","," ")
	s = s.replace("!"," ")
	s = s.replace("?"," ")
	s = s.replace("-"," ")
	s = s.replace("_"," ")
	return s