def retira_pontuacao(txt):
    """ fornecida uma frase a função retornara uma frase onde
    os caracteres de pontuação serao substituidos por espaço"""
    txt1= txt.replace('.',',')
    txt2= txt1.replace(',','-')
    txt3= txt2.replace('-',';')
    txt4= txt3.replace(';',':')
    txt5= txt4.replace(':','?')
    txt6= txt5.replace('?','!')
    txt7= txt6.replace('!',' ')
    return(txt7)