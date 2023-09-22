def inverte(frase):
    '''Função que pega a frase de entrada, e retorna a frase com as pontuações retiradas, 
    com as palavras em minúsculo e invertida 
    str,str→str'''
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
	frase2=",".join(lista)
    frase3= frase2.replace(',',' ')
    return frase3