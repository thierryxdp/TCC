def retira_pontuacao(frase):
    '''retorna a frase sem pontuação
    str->str'''
    semunder=str.replace(frase,'_',' ')
    semvir=str.replace(semunder,',',' ')
    semdois=str.replace(semvir,':',' ')
    sempontovir=str.replace(semdois,';',' ')
    semexcla=str.replace(sempotovir,'!',' ')
    seminter=str.replace(semexcla,'?',' ')
    semponto=str.replace(seminter,'.',' ')
    return semreti=str.replace(semponto,'...',' ')