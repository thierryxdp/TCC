de uppCons (frase):
    """Retorna uma dada frase com as suas consoantes em caixa alta.
    Entrada: str
    Saída: str
    """
    contagem = 0
    resultado = ''
    while contagem < len(frase):
        letra = frase[contagem]
        if letra in 'bcçdfghjklmnpqrstvwxyz':
            letra = str.upper(letra)
        resultado += letra
        contagem += 1
    return resultado