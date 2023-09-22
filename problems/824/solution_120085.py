def uppCons(text):
    """Recebe um texto e torna sua consoantes em maiúsculo;
    str --> str"""

    consoantes_min = "qwrtypsdfghjklçzxcvbnm"
    buffer = ""
    iii = 0
    
    while (iii < len(text)):
        if (text[iii] in consoantes_min):
            # Adiciona a consoante em maiuscula ao buffer
            buffer += str.upper(text[iii])
        else:
            buffer += text[iii]
        iii += 1    
    return buffer