import re
def retira_pontuacao(frase):
    x = re.sub(r"[,;&!?/.:]", frase, "")
    return x