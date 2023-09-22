def conta_frases(frases):
    interrogacao = str.count(frases, '?')
    exclamacao = str.count(frases, '!')
    ponto = str.count(frases, '.')
    pontopontoponto = str.count(frases, '...')
    pontocerto = ponto - pontopontoponto
                            
    return '''interrogacao + exclamacao + pontocerto +''' pontopontoponto