def conta_frases(texto_armazenado):
    """Funcao que recebe um texto armazenado em uma string e retorna o numero de frases que este texto tem. str=>int"""
    texto_armazenado=str.replace(texto_armazenado,'...','#')
    return str.count(texto_armazenado,'?')+str.count(texto_armazenado,'#')+str.count(texto_armazenado,'.')