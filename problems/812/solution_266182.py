def retira_pontuacao(texto):
    operacao = str.replace(texto,",",' ') and str.replace(texto,'.',' ') and str.replace(texto,'—',' ') and str.replace(texto,':',' ') and str.replace(texto,';',' ') and str.replace(texto,'!',' ') and str.replace(texto,'?',' ') and str.replace(texto,'',' ')
    return operacao