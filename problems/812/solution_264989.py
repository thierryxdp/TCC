def retira_pontuacao(texto):
    x=str.replace(texto,'-',' ')(texto,',',' ')(texto,':',' ')(texto,';',' ')(texto,'.',' ')
    return x