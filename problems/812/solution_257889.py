def retira_pontuacao(frase):
    ''''retorna a frase dada sem qualquer pontuação
    str->str'''
    s=frase
    f1=s.split('!')
    f2=str.join(' ',f1)
    f3=f2.split('.')
    f4=str.join(' ',f3)
    f5=f4.split(',')
    f6=str.join(' ',f5)
    f7=f6.split('-')
    f8=str.join(' ',f7)
    f9=f8.split('?')
    return str.join(' ',f9)