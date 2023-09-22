def lingua_p(palavra):
    """funcao que retorna uma palavra que foi dada traduzida da lingua do P.
    str -> str"""
    traduzida = ''
    contagem = 0
    while contagem <len(palavra):
        if palavra[contagem] in 'AEIOUaeiouáéíóúãõ':
            traduzida = traduzida + palavra[contagem]+'p'+palavra[contagem]
        else:
            traduzida += palavra[contagem]
            contagem += 1
    return str.lower(traduzida)