def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
	troca = frase.replace('.',' ')
    troca2 = troca.replcae(',',' ')
    return troca2