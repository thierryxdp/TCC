def retira_pontuacao(frase):
    '''
    funcao que recebe uma frase em string e retorna
    essa mesma frase, mas com todos os sinais de
    pontuacao removidos e substituidos por espaco
    string->string
    '''
    travessao=frase.replace('-',' ')
    virgula=travessao.replace(',',' ')
    doisPontos=virgula.replace(':',' ')
    pontoEvirgula=doisPontos.replace(';',' ')
    ponto=pontoEvirgula.replace('.',' ')
    exclamacao=ponto.replace('!',' ')
    interrogacao=exclamacao.replace('?',' ')
    reticencias=interrogacao.replace('...',' ')
    frasefinal=reticencias
    return frasefinal