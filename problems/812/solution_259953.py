def retira_pontuacao(frase):
    '''funcao que dada uma frase retira todos os 
    caracteres de potuação'''
    f1=frase.replace('!','')
    f2=f1.replace('.','')
    f3=f2.replace(',','')
    f4=f3.replace(':','')
    f5=f4.replace('/','')
    f6=f5.replace('?','')
    f7=f6.replace(':','')
    f8=f7.replace(';','')
    f9=f8.replace('...','')
    return frase