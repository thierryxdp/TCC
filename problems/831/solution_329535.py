def lingua_p(palavra):
    """Retorna uma dada palavra traduzida para a língua do P em letras minúsculas.
    Entrada: str
    Saída: str
    """
    traduzida = palavra
    contagem = 0
    for n in palavra:
        if n in 'AEIOUaeiou':
            traduzida = traduzida[0:(contagem+1)]+'p'+traduzida[0:]
        contagem += 1
    return str.lower(traduzida)