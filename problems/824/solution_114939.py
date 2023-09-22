def uppCons (frase):
    """Retorna uma dada frase com as suas consoantes em caixa alta.
    Entrada: str
    Saída: str
    """
    contagem = 0
    resultado = ''
    while contador < len(frase):
        letra = frase[contagem]
        if caractere not in 'AEIOUaeiou':
            letra = str.upper(letra)
        resultado += letra
        contador += 1
    return resultado