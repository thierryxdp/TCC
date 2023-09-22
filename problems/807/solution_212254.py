def conta_frase(frase):
    """Verifica a quantidade de frase em um string;
    str -> int"""
	resultado = frase.count("! ")+frase.count("? ")+frase.count(". ")+frase.count("... ")
    if frase[-1] == "?" or frase[-1] == "!" or frase[-1] == "..." or frase[-1] == ".":
		resultado -=1
    return resultado