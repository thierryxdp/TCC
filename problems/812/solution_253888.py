def retira_pontuacao(frase):
    if '-.,:?;!' in frase:
        return replace(frase, '-.,:?;!', ' ')
    else:
        return frase