def retira_pontuacao(frase):
    """tem como entrada uma frase, na qual são retiradas todas as pontuações, retornando a frase com espaço no lugar das pontuações. str->str"""
    
    ponto=frase.replace('.',' ')
    virgula=ponto.replace(',',' ')
    pontovirg=virgula.replace(';',' ')
    exclamacao=pontovirg.replace('!',' ')
    interrogacao=exclamacao.replace('?',' ')
    travessao=interrogacao.replace('-',' ')
    reticencia=travessao.replace('...',' ')
    ponto2=reticencia.replace(':',' ')
    return ponto2