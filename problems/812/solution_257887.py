def retira_pontuacao(frase):
    s=frase
    f1=s.split('!')
    f2=str.join(' ',f1)
    f3=f2.split('.')
    f4=str.join(' ',f3)
    f5=f4.split(',')
    f6=str.join(' ',f5)
    f7=f6.split('-')
    return str.join(' ',f7)