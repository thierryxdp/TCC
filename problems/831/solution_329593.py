def lingua_p(palavra):
    """Retorna uma dada palavra traduzida para a língua do P em letras minúsculas.
    Entrada: str
    Saída: str
    """
    traduzida = ''
    resposta = 'supustipivépérepeipis'
    contagem = 0
    while contagem < len(palavra):
        if palavra[contagem] in 'AEIOUaeiouáéíóúãõ':
            traduzida = traduzida + palavra[contagem] + 'p' + palavra[contagem]
        else:
            traduzida += palavra[contagem]
        contagem += 1
    return str.lower(traduzida)