def inverte(ponto):

    frase=ponto.split(' ')

    list.reverse(frase)

    ponto2=frase.replace('.',' ')

    virgula=ponto2.replace(',',' ')

    pontovirg=virgula.replace(';',' ')

    exclamacao=pontovirg.replace('!',' ')

    interrogacao=exclamacao.replace('?',' ')

    travessao=interrogacao.replace('-',' ')

    reticencia=travessao.replace('...',' ')

    ponto3=reticencia.replace(':',' ')
    return''.join(ponto3)