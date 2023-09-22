def retira_pontuacao(frase):
    """ Função que recebe um argumento em forma de frase e retorna a mesma frase com as pontuaçaões 
    trasformadas em espaços """
    
    interrogacao = str.replace(frase, "?", " ")
    exclamacao = str.replace(interrogacao, "!", " ")
    pontoFinal = str.replace(exclamacao, ".", " ")
    travessao = str.replace(pontoFinal, "-", " ")
    virgula = str.replace(travessao, ",", " ")
    doisPontos = str.replace(virgula, ":", " ")
    pontoVirgula = str.replace(doisPontos, ";", " ")
    return pontoVirgula