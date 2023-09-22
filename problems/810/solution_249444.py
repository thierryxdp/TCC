def inverte(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
	troca = frase.replace('.',' ')
    troca2 = troca.replace(',',' ')
    troca3 = troca2.replace('-',' ')
    troca4 = troca3.replace(':',' ')
    troca5 = troca4.replace(';',' ')
    troca6 = troca5.replace('!',' ')
    troca7= troca6.replace('?',' ')
    minusculo=troca7.lower()
	lista= minusculo.split()
	lista.reverse()
	''.join(lista)
    return frase2