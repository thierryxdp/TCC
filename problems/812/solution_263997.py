def retira_pontuação(texto):
    '''função que substitui as pontuações por espaços
    str->str'''
    a=' '.join(texto.split(','))
    b=' '.join(texto.split('-'))
    c=' '.join(texto.split(':'))
    d=' '.join(texto.split(';'))
    e=' '.join(texto.split('.'))
    
    return e