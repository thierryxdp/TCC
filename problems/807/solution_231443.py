def conta_frases(frase):
    pontofinal=str.count(frase,'.')-((str.count(frase,'...'))*3)
    interrogacao=str.count(frase,'?')
    exclamacao=str.count(frase,'!')
    trespontos=str.count(frase,'...')
    numerodefrases=pontofinal+interrogacao+exclamacao+trespontos
    return numerodefrases