def retira_pontuacao(string):
    """Retorna a string com seus caracteres de pontuação substituidos por espaço;
    string -> string"""
    travessao = string.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_pontos = virgula.replace(':', ' ')
    ponto_virgula = dois_pontos.replace(';', ' ')
    reticencias = ponto_virgula.replace('...', ' ')
    p_exclamacao = reticencias.replace('!', ' ')
    p_interrogacao = p_exclamacao.replace('?', ' ')
    p_final = p_interrogacao.replace('.', ' ')
    return p_final