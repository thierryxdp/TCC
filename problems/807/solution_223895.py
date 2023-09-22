def conta_frases(texto):
    retic = texto.count("...")
    texto1 = str.replace(texto,"..."," ")
    p_final = texto1.count(".")
    p_interr = texto1.count("?")
    p_exclam = texto1.count("!")
    
    return p_final + p_interr + p_exclam + retic