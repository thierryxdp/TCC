def retira_pontuacao(frase):
    """Dada uma frase pontuada, remo vetodos os pontos como travessao, virgula, dois pontos,
    e ponto final substituindo por espaço,
     str -> str"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doispontos = virgula.replace(':', ' ')
    pontovirgula = doispontos.replace(';', ' ')
    pontofinal = pontovirgula.replace('.', ' ')
    pontointerrogacao = pontofinal.replace('?', ' ')
    pontoExclamacao = pontointerrogacao.replace('!', ' ')
    return pontoExclamacao

def inverte(frase):
    """A função remove as pontuações da frase, substitui as letras maisculas
    por minusculas e inverte a frase:
    str -> str"""
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('!', ' ')
    frase = str.lower(frase)
    frase = frase.split()
    frase = " ".join(frase)
    return frase