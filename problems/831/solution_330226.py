def lingua_p(palavra):
    """
    Função recebe uma palavra como parâmetro, e retorna essa mesma palavra
    traduzida para a lingua do P.
    str -> str
    """
    vogais="aeiouáéíóúAEIOUÁÉÍÓÚ"
    linguap=""
    for i in palavra:
        if i in vogais:
            linguap+=i+"p"+i
        else:
            linguap+=i
    return str.lower(linguap)