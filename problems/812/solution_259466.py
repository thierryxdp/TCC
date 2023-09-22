# Retira caracteres de pontuação de um texto
# str -> str
def retira_pontuacao(t):
    t.replace('-', '').replace(',', '').replace(':', '').replace(';', '').replace('.', '')