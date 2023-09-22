def retira_pontuacao(string):
    """Retorna a string com seus caracteres de pontuação substituidos por espaço;
    string -> string"""
    travessao = string.replace('-', ' ')
    virgula = travessao.replace(',', '')
    dois_pontos = virgula.replace(':', '')
    ponto_virgula = dois_pontos.replace(';', '')
    reticencias = ponto_virgula.replace('...', '')
    p_exclamacao = reticencias.replace('!', '')
    p_interrogacao = p_exclamacao.replace('?', '')
    p_final = p_interrogacao.replace('.', '')
    return p_final

#5

def inverte(string):
    """Retorna a frase com as palavras na ordem inversa, sem pontuação
    e toda em letras minúsculas;
    string -> string"""
    string = string.lower()
    string = retira_pontuacao(string)
    l = string.split(" ")
    li = l[::-1]
    return str.strip(str.join(' ', li))