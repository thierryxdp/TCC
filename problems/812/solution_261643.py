def retira_pontuacao(txt):
    return ('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')