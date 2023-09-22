def lingua_p(palavra):
    """
    
    """
    vogais="aeiouáéíóúAEIOUÁÉÍÓÚ"
    linguap=""
    for i in palavra:
        if i in vogais:
            linguap+=i+"p"+i
        else:
            linguap+=i
    return str.lower(linguap)