def retira_pontuacao(frase):
    '''
    Ao inserir uma string, substitui virgulas, pontos,
    pontos e virgula, dois pontos, etc por um espaço.
    str -> str
    '''
    x = frase.replace("."," ")
    x = x.replace(","," ")
    x = x.replace(";"," ")
    x = x.replace(":"," ")
    x = x.replace("-"," ")
    x = x.replace("?"," ")
    x = x.replace("!"," ")
    return x