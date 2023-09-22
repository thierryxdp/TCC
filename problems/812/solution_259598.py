import re 
def retira_pontuacao(texto):
    substituido = re.sub(r'[^\w\s]', '', texto)

    return substituido