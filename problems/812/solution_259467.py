# Retira caracteres de pontuação de um texto
# str -> str
def retira_pontuacao(t):
    return t.replace('-', '').replace(',', '').replace(':', '').replace(';', '').replace('.', '')