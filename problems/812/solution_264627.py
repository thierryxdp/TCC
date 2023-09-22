def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
	troca = frase.replace('.',' ')
    troca2 = troca.replace(',',' ')
    return troca2