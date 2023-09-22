def lingua_p(palavra):
    """Retorna uma dada palavra traduzida para a língua do P em letras minúsculas.
    Entrada: str
    Saída: str
    """
    traduzida = palavra
    contagem = 0
    while contagem < len(palavra):
        if palavra[contagem] in 'AEIOUaeiou':
            traduzida = traduzida[0:(contagem+1+str.count(traduzida, 'p'))]+'p'+palavra[contagem]+traduzida[(contagem+1):]
        contagem += 1
    return str.lower(traduzida)