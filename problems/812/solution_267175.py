def retira_pontuacao(texto):
    '''função que substitui as pontuações em um texto, (texto), por espaço'''
    '''entrada:(texto),um texto da escolha do usuário
    saída: o texto,porém sem as pontuações'''
    x=texto.replace('.',' ')
    y=x.replace('!',' ')
    w=y.replace('?',' ')
    z=w.replace('-',' ')
    a=z.replace(',',' ')
    b=a.replace(':',' ')
    c=b.replace(';',' ')
    if '.'or'!'or'?'or'-'or','or':'or';'in texto:
        return c