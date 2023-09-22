def conta_frases(frase):
    pontofinal=str.count(frase,'.')
    interrogacao=str.count(frase,'?')
    exclamacao=str.count(frase,'!')
    trespontos=str.count(frase,'...')
    numerodefrases=pontofinal+interrogacao+exclamacao+trespontos
    return numerodefrases