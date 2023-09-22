def retira_pontuacao(texto):
    ''' essa função remove a pontuação da frase substituindo por espaços;str->str'''
    f1=(str.replace(texto,'!',' '))
    f2=(str.replace(f1,':',' '))
    f3=(str.replace(f2,'?',' '))
    f4=(str.replace(f3,'.',' '))
    f5=(str.replace(f4,'-',' '))
    f6=(str.replace(f5,';',' '))
    f7=(str.replace(f6,'...',' '))
    f8=(str.replace(f7,',',' '))
    return f8
def inverte(frase):
    ''' função que inverte e retira pontos de uma frase;str->lis'''
    fase1=(retira_pontuacao(frase))
    fase2=str.lower(fase1)
    fase3=str.split(fase2)
    fase4=fase3(::-1)
    return str.join(' ',fase4)