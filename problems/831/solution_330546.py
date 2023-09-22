def lingua_p(palavra):
    """
    Essa função recebe uma palavra e retorna ela na língua do P;
    str -> str
    """
    vogais = 'aáàãeéêiíoóôuú'
    resultado = ''
    palavra_min = palavra.lower()
    for i in palavra_min:
        resultado += i
        if i in vogais:
            resultado += 'p'
    return resultado