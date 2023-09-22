def retira_pontuacao(frase):
    '''Funçao que pega a frase de entrada e retorna a troca das pontuações por espaço
    str,str→str'''
    pontuacao=['-',',',':',';','.']
	troca = frase.replace('.',' ')
    troca2 = troca.replace(',',' ')
    troca3 = troca2.replace('-',' ')
    troca4 = troca3.replace(':',' ')
    troca5 = troca4.replace(';',' ')
    troca6 = troca5.replace('!',' ')
    troca7= troca6.replace('?',' ')
    return troca7

def inverte(frase):
    ''' '''
    lista= frase.split(' ')
    inverte= lista.sort(lista, reverse=True)
    juncao= join(inverte)
   	return juncao