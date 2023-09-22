def conta_frases(texto):
    '''função responsável por contar o número de frases em um texto,(texto),de escolha do usuário'''
    x=texto.split(.)
    y=x.split(!)
    z=y.split(?)
    w=z.split(...)
    return len(w)