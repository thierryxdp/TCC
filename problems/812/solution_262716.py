def retira_pontuacao(frase):
    '''funcao que substitui pontuacoes por espacos.str->str'''
    frase_nova1=str.replace(frase,'.',' ')
    frase_nova2=str.replace(frase_nova1,',',' ')
    frase_nova3=str.replace(frase_nova2,'?',' ') 
    frase_nova4=str.replace(frase_nova3,'!',' ')
    frase_nova5=str.replace(frase_nova4,'-',' ')
    return frase_nova5