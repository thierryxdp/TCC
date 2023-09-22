def retira_pontuacao(frase):
    """Dada uma frase pontuada, remove todos os pontos como travessao, virgula, dois pontos,
    e ponto final substituindo por espaço,
     str -> str"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    def  inverte ( frase ):
    lista  =  str . divisão ( frase )
    lista . reverso ()
    frase  =  str . juntar ( "" , lista )
     return frase