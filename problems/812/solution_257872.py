def retira_pontuacao(frase):
    s=frase
    f1=str(s.split('!'))
    f2=str(f1.split('.'))
    f3=str(f2.split(','))
    f4=str(f3.split('?'))
    f5=str(f4.split(':'))
    return str.join(' ',f5)