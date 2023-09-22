#Função que dada uma frase como entrada, retorna a frase onde a pontuação é substituida por espaços s caracteres de po
def retira_pontuacao(fraseInicial):
    travessao = str.replace(fraseInicial,'-',' ')
    virgula = str.replace(travessao,',',' ')
    doisPontos = str.replace(virgula,':',' ')
    pontoVirgula = str.replace(doisPontos,';',' ')
    pontoFinal = str.replace(pontoVirgula,'.',' ')
    pontoInterrogacao = str.replace(pontoFinal,'?',' ')
    pontoExclacamacao = str.replace(pontoInterrogacao,'!',' ')

    return pontoExclacamacao