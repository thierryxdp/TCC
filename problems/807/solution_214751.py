def conta_frases(texto):
    ''' iniciamos a contagem retirando o número
    excedentes de pontos, assim podemos aproveeitar da contagem recursiva
    que o programa faz'''
    numero=texto.count('...')*(-2)
    numero+=texto.count('!')
    numero+=texto.count('?')
    numero+=texto.count('.')
    if numero == 0:
        numero+= 1
        return numero
    else:
        return numero