def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
	troca = frase.replace('.',' ')
    troca2 = troca.replace(',',' ')
    troca3 = troca2.replace('-',' ')
    troca4 = troca3.replace(':',' ')
    troca5 = troca4.replace(';',' ')
    return troca5