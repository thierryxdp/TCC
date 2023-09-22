def retira_pontuacao(frase):
    x = str.replace(frase, '-', ' ')
    y = str.replace(x, ',', ' ')
    z = str.replace(y, ':', ' ')
    a = str.replace(z, ';', ' ')
    b = str.replace(z, '.', ' ')
    
    
	return b