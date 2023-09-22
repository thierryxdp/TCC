def conta_frases(frases):
    lista1=frases.split('?')
    lista2=frases.split('.')
    lista3=frases.split('...')
    lista4=frases.split('!') 
    return len(lista1)+len(lista2)+len(lista3)+len(lista4)