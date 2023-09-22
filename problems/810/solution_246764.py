def inverter(txt):
    """função que inverte a ordem das palavras e remove sua pontuação"""
  	'str->str'
    txt1= txt.replace('.',',')
    txt2= txt1.replace(',','-')
    txt3= txt2.replace('-',';')
    txt4= txt3.replace(';',':')
    txt5= txt4.replace(':','?')
    txt6= txt5.replace('?','!')
    txt7= txt6.replace('!',' ')
  	inversa= ' '.join(reversed(txt7))
    return txt7