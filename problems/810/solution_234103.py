def retira_pontuacao(frase):
    """Função que dada uma frase retira todos os caracteres de pontuação e os substitui por espaço
    str -> str"""
    travessao = str.replace(frase, '-', ' ')
    virgula = str.replace(travessao, ',', ' ')
    doispontos = str.replace(virgula, ':', ' ')
    pontovirgula = str.replace(doispontos, ';', ' ')
    ponto = str.replace(pontovirgula, '.', ' ')
    exclamacao = str.replace(ponto, '!', ' ')
    interrogacao = str.replace(exclamacao, '?', ' ')
    return interrogacao

def inverte(frase):
    """Funcao que dada uma frase, inverte suas palavras, remove a pontuação e retira as letras maiúsculas, retornando uma
    nova frase
    str -> str"""
    SemPontuacao = retira_pontuacao(frase)
    Minusculas = str.lower(SemPontuacao)
    Separa = str.split(Minusculas)
    Inverte = Separa[::-1]
    Junta = str.join(' ', Inverte)
    return Junta