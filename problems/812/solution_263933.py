def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna ela com os caracteres de pontuação substituídos por espaço
    str -> str'''
    nova1=srt.replace(frase,',',' ')
    nova2=srt.replace(nova1,'-',' ')
    nova3=srt.replace(nova2,':',' ')
    nova4=srt.replace(nova3,';',' ')
    nova5=srt.replace(nova4,'...',' ')
    nova6=srt.replace(nova5,'.',' ')
    nova7=srt.replace(nova6,'!',' ')
    nova8=srt.replace(nova7,'?',' ')
    return nova8