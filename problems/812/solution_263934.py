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