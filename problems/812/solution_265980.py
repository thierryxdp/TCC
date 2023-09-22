def retira_pontuacao(frase):
    '''Essa função substitui caracteres de pontuação por espaço
    str -> str'''
    final = frase.replace("."," ")
    interrogacao = final.replace("?", " ")
    exclamacao = interrogacao.replace("!", " ")
    travessao = exclamacao.replace("-", " ")
    virgula = travessao.replace(",", " ")
    pontos = virgula.replace(":", " ")
    pontovirg = pontos.replace(";", " ")
    return pontovirg