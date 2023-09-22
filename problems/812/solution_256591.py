import re
def retira_pontuacao(frase):
    valor = frase + '-,:;.!?'
    s = re.sub('[-,:;.!?]',' ',valor)
    return valor