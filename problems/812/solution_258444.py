import re
def retira_pontuacao(frase):
    '''retira as pontuações da frase substituindo por espaços
    str -> str'''
    pontuacoes = ['.','-',',',':',';','!','?']
    return re.sub(r"[,;!?.:]", frase, "")