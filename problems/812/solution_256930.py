"Função que retorna um texto sem a pontuação"
def retira_pontuacao(texto):
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'.',' ')
    return texto