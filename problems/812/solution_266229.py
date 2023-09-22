import re
def retira_pontuacao(texto):
    operacao = re.sub('[,:—;!?.]',' ', texto)
    return operacao