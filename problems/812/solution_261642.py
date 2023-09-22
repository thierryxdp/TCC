def retira_pontuacao(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')