def conta_frases(frase):
    """..."""
    count_interrogacao = str.count(frase,'?')
    count_exclamacao = str.count(frase,'!')
    count_trespontos = str.count(frase,'...')
    count_pontofinal = str.count(frase,'.') - 3*count_trespontos
    
    return count_interrogacao + count_exclamacao + count_pontofinal + count_trespontos