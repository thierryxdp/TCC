def retira_pontuacao (frase, pontuacao):
    if frase in pontuacao:
        return str.replace (frase, pontuacao, ' ')