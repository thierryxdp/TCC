def conta_frases(x):
    beta=x.replace('...','.')
    A=beta.count('.')
    B=beta.count('!')
    C=beta.count('?')
    return A+B+C