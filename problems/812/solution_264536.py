def retira_pontuacao(frase):
        f1 = str.join(' ', str.split(frase, '-'))
    	f2 = str.join(' ', str.split(f1, ','))
    	f3 = str.join(' ', str.split(f2, ':'))
    	f4 = str.join(' ', str.split(f3, ';'))
    	f5 = str.join(' ', str.split(f4, '.'))
    	f6 = str.join(' ', str.split(f5, '?'))
    	f7 = str.join(' ', str.split(f6, '!'))
    	return f7