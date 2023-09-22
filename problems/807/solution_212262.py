def conta_frase(frase):
    """Verifica a quantidade de frase em um string;
    str -> int"""
    resultado = frase.count("! ")+frase.count("? ")+frase.count(". ")+frase.count("... ")
    if "?" or "!" or "..." or ".":
        resultado +=1
    return resultado