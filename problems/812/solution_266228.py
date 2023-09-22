def retira_pontuacao(texto):
    import re
    operacao = re.sub('[,:—;!?.]',' ', texto)
    return operacao