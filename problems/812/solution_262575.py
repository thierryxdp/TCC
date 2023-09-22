def retira_pontuacao(frase):
    '''Troca todas as pontuações por espaço
    str->str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'/',' ')
    return frase