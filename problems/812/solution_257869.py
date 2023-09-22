def retira_pontuacao(frase):
    s=frase
    f1=s.split('!')
    f2=f1.split('.')
    f3=f2.split(',')
    f4=f3.split('?')
    f5=f4.split(':')
    return str.join(' ',f5.split('!'))