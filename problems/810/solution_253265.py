def inverte(frase):

    ponto=frase.replace('.',' ')

    virgula=ponto.replace(',',' ')

    pontovirg=virgula.replace(';',' ')

    exclamacao=pontovirg.replace('!',' ')

    interrogacao=exclamacao.replace('?',' ')

    travessao=interrogacao.replace('-',' ')

    reticencia=travessao.replace('...',' ')

    ponto2=reticencia.replace(':',' ')


    ponto3=ponto2.split(' ')

    list.reverse(ponto3)
    'ponto3'.strip(ponto3,' ')

    return' '.join(ponto3)