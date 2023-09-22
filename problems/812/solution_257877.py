def retira_pontuacao(frase):
    s=frase
    f1=s.split('!')
    f2=str.join(' ',f1)
    f3=f2.spli(',')
    
    return str.join(' ',f3)