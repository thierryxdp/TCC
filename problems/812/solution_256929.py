"Função que retorna um texto sem a pontuação"
def retira_pontuacao(texto):
    texto= str.replace(texo,'-',' ')
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(tetxo,'.',' ')
    return texto