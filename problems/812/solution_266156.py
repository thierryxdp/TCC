def retira_pontuacao(texto):
    operacao = (str.strip(texto,'—')and str.strip(texto,',') and str.strip(texto,':') and str.strip(texto,';') and str.strip(texto,'.'))
    return operacao