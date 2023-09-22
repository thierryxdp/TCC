def conta_frases3(frases):
    lista1=list(frases.count('.'))
    lista2=list(frases.count('?'))
    lista3=list(frases.count('!'))
    lista4=list(frases.count('...'))
    return lista1+lista2+lista3+lista4