def conta_frases(texto):
    """função que retorna a quantidade de frases presente no texto
    str -> int"""
    quant_interrogacao = str.count(texto,'?')
    quant_exclamacao = str.count(texto,'!')
    quant_trespontos = str.count(texto,'...')
    quant_pontofinal = str.count(texto,'.') - quant_trespontos*3
    return quant_interrogacao + quant_exclamacao + quant_trespontos + quant_pontofinal