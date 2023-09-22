def conta_frases(frase):
    """Funcao que retorna o numero de frases em um determinado texto.Porem,
    apenas frases terminadas em ?,. e ! serao contadas na funcao"""
    string_pontuacao=frase.replace('!','.')
    string_pontuacao=string_pontuacao.replace('?','.')
    string_pontuacao=string_pontuacao.replace('...','.')
    return string_pontuacao.count('.')