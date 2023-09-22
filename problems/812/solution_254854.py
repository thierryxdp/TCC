def retira_pontuacao(texto):
    """Função para retirar toda a pontuação de um texto.
       Onde: "texto" - é o texto em que se deseja retirar a pontuação.
    str -> str """
    novo = texto.replace('.', ' ')
    novo = novo.replace('!', ' ')
    novo = novo.replace('?', ' ')
    novo = novo.replace('-', ' ')
    novo = novo.replace(',', ' ')
    novo = novo.replace(':', ' ')
    novo = novo.replace(';', ' ')
    return texto7