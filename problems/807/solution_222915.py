def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    if '.' in texto:
        a = 1
        elif '.' not in texto:
            a = 0
            if '!'in texto:
                b = 1
                elif'!' not in texto:
                    b = 0
                    if '?' in texto:
                        c = 1
                        elif '?' not in texto:
                            c = 0
                            if '...' in texto:
                                d = 1
                                elif '...' not in texto:
                                    d = 0
                                    return a+b+c+d