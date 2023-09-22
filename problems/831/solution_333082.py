def lingua_p(palavra):
    """doc"""
    palavra = palavra.lower()
    vogais = ['a','à', 'á', 'ã', 'â', 'e', 'é', 'è', 'ê', 'i', 'í', 'ì', 'o', 'ò', 'ó', 'ô', 'õ', 'u', 'ú', 'ù']
    traducao = []
    for letra in palavra:
        if letra in vogais:
            traducao.append(letra + 'p' + letra)
        else:
            traducao.append(letra)
    return ''.join(traducao)