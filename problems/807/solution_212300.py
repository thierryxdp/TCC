def conta_frases(frase):
    """Verifica a quantidade de frase em um string;
    str -> int"""    
    global nova_frase
    resultado = 0
    if "..." in frase:
        resultado += frase.count("...")
        nova_frase = frase.replace("... ", " ", len(frase))
        resultado += nova_frase.count("!") + nova_frase.count("?") + nova_frase.count(".")
    else:
        resultado += frase.count("!") + frase.count("?") + frase.count(".")
    return resultado