def retira_pontuacao(frase):
    '''retorna a frase informada com todos os caracteres de pontuação substituidos por um espaço
    str -> str'''
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(frase,',',' ')
    dois_pts = str.replace(frase,':',' ')
    ponto_virg = str.replace(frase,';',' ')
    ponto = str.replace(frase,'.',' ')
    exclamacao = str.replace(frase,'!',' ')
    interrogacao = str.replace(frase,'?',' ')
    return travessao(virgula(dois_pts(ponto_virg(ponto(exclamacao(interrogacao))))))