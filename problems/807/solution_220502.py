def conta_frases(f):
    " Conta a quantidade de caracteres específicos levando que cada frase possui apenas 1 deles. string -> int"
    fAlterado = f.replace('...', '#')
    frases = fAlterado.count('!')
    frases += fAlterado.count('.')
    frases += fAlterado.count('?')
    frases += fAlterado.count('#')
    
    return frases