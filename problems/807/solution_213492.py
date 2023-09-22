def conta_frase(frase):
    ''' funcao que conta quantas frases ha no parametro dado. str -> int'''
    ponto = frase.count('.')
    tres_pontos = frase.count('...')
    exclamacao = frase.count('!')
    interrogacao = frase.count('?')
    
    if tres_pontos != 0:
        ponto = ponto - 3*tres_pontos
        
    return ponto + tres_pontos + exclamacao + interrogacao