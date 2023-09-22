def retira_pontuacao(frase):
    '''retorna a frase informada com todos os caracteres de pontuação substituidos por um espaço
    str -> str'''
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(travessao,',',' ')
    dois_pts = str.replace(virgula,':',' ')
    ponto_virg = str.replace(dois_pts,';',' ')
    ponto = str.replace(ponto_virg,'.',' ')
    exclamacao = str.replace(ponto,'!',' ')
    interrogacao = str.replace(exclamacao,'?',' ')
    return interrogacao