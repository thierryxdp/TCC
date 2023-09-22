def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
	troca = frase.replace('.',' ')
    troca2 = troca.replace(',',' ')
    troca3 = troca2.replace('-',' ')
    troca4 = troca3.replace(':',' ')
    troca5 = troca4.replace(';',' ')
    troca6 = troca5.replace('!',' ')
    troca7= troca6.replace('?',' ')
    return troca7