def lingua_p(palavra):
    traduzida = ''"
    contagem = 0
    while contagem < len(palavra):
        if palavra[contagem] in 'AEIOUaeiouáéíóúãõ':
            traduzida = traduzida + palavra[contagem] + 'p' + palavra[contagem]
        else:
            traduzida += palavra[contagem]
        contagem += 1
    return str.lower(traduzida)