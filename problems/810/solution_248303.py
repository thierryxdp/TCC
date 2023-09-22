def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna ela com os caracteres de pontuação substituídos por espaço
    str -> str'''
    nova1= str.replace(frase,',',' ')
    nova2= str.replace(nova1,'-',' ')
    nova3= str.replace(nova2,':',' ')
    nova4= str.replace(nova3,';',' ')
    nova5= str.replace(nova4,'...',' ')
    nova6= str.replace(nova5,'.',' ')
    nova7= str.replace(nova6,'!',' ')
    nova8= str.replace(nova7,'?',' ')
    return nova8

def inverte(frase):
	'''Função que inverte a ordem das palavras da frase, troca letras maiúsculas por minúsculas e retira a pontuação da frase.
    str -> str'''
    f1= str.lower(frase)
    f2= retira_pontuacao(f1)
    f3= str.split(f2)
    f4= list.reverse(f3)
    
    return f2