def retira_pontuacao (frase):
   a = frase.replace (',',' ')
   b = frase.replace (';', ' ')
   c = frase.replace (':', ' ')
   d = frase.replace ('.', ' ')
   e = frase.replace ('-', ' ')
	return a,b,c,d,e