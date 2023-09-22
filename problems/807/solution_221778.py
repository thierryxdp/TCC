def conta_frases(frases):
    lista1=list(frases)
    lista2=list(frases)
    lista3=list(frases)
    lista4=list(frases)
    lista1=frases.count('?')
    lista2=frases.count('.')
    lista3=frases.count('...')
    lista4=frases.count('!') 
    return lista1+lista2+lista3+lista4