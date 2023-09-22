def retira_pontuacao(frase):
    nova0=str.replace(frase,'...','$')
    nova=str.replace(nova0,'-',' ')
    nova1=str.replace(nova,',',' ')
    nova2=str.replace(nova1,':',' ')
    nova3=str.replace(nova2,';',' ')
    nova4=str.replace(nova3,'.',' ')
    nova5=str.replace(nova4,'!',' ')
    nova6=str.replace(nova5,'?',' ')
    nova7=str.replace(nova6,'$',' ')
    return nova7