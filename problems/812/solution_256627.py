def retira_pontuacao(frase):
    '''descricao '''
    virgula = str.replace(frase,","," ")
    doispontos = str.replace(frase,":"," ")
    ponto = str.replace(frase,"."," ")
    return frase