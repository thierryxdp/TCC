def retira_pontuacao(frase):

    ponto=frase.replace('.',' ')

    virgula=ponto.replace(',',' ')

    pontovirg=virgula.replace(';',' ')

    exclamacao=pontovirg.replace('!',' ')

    interrogacao=exclamacao.replace('?',' ')

    travessao=interrogacao.replace('-',' ')

    reticencia=travessao.replace('...',' ')

    ponto2=reticencia.replace(':',' ')

    return ponto2