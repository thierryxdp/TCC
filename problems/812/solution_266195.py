def retira_pontuacao(texto):
    operacao = str.replace(texto,',',' ')
    operacao = str.replace(texto,':',' ')
    operacao = str.replace(texto,'—',' ')
    operacao = str.replace(texto,':',' ')
    operacao = str.replace(texto,';',' ')
    operacao = str.replace(texto,'!',' ')
    operacao = str.replace(texto,'?',' ')
    return operacao