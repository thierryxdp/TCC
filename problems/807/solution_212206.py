def conta_frases(frase):
    """Verifica e retorna a quantidade de frases separadas por (.,!,?,...) contida em uma string;
    str->int"""
    resultado = frase.count("! ")+frase.count("?  ")+frase.count(". ")+frase.count("... ")
    return resultado