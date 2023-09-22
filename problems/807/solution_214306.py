def conta_frases(texto):
    """função que retorna a quantidade de frases presente no texto
    str -> int"""
    quant_interrogação = str.count(texto,'?')
    quant_exclamação = str.count(texto,'!')
    quant_trespontos = str.count(texto,'...')
    quant_pontofinal = str.count(texto,'.') - quant_trespontos*3
    return quant_interrogação + quant_exclamação + quant_trespontos + quant_pontofinal